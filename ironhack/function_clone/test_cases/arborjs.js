import ddf.minim.*;
import org.json.*;
import traer.physics.*;
//import traer.animation.*;

final float NODE_SIZE = 17;
final float EDGE_LENGTH = 250;
final float EDGE_STRENGTH = 0.2;
final float SPACER_STRENGTH = 1000;

Vector songs;
int currentSong;
PFont legendFont, labelFont, boxFont;
int sylCounter;
int selNode;

color sylPalette[] = {#B7B697, #755522, #696C57, #B2862D, #914520, #639A41, #94D16E, 
                      #D9D362, #DDE2B7, #ABCDDD, #E8A07D, #1F998F, #BEBAD1, #8896AD};
int numRows, numCols, boxSize;

//
// P5 routines
//

void setup(){
    size( 700, 700 );
    Minim.start(this);
    smooth();
    songs = new Vector(10);
    songs.addElement(new SyntaxNet("bk42w74.json"));
    songs.addElement(new SyntaxNet("bk43w73.json"));
    songs.addElement(new SyntaxNet("bk70bk62.json"));
    songs.addElement(new SyntaxNet("bk95bk3.json"));
    songs.addElement(new SyntaxNet("g81w58.json"));
    songs.addElement(new SyntaxNet("g83w57.json"));
    songs.addElement(new SyntaxNet("pk60gr7.json"));
    songs.addElement(new SyntaxNet("r15bl29.json"));
    songs.addElement(new SyntaxNet("r17pu46.json"));
    println("Added "+songs.size()+" songs");
        
    currentSong = 0;
    SyntaxNet newNet = (SyntaxNet)songs.elementAt(currentSong);
    newNet.makeActive();
    legendFont = loadFont("RockwellStd-20.vlw");
    labelFont = loadFont("CaspariCaps-Bold-12.vlw");
    boxFont = loadFont("CaspariCaps-26.vlw");
    sylCounter = -1;


    // Set up the size of the syllable boxes area
    numRows = 5;
    numCols = 20;
    boxSize = width/numCols;
    
}

void draw(){
    SyntaxNet net = (SyntaxNet)songs.elementAt(currentSong);
    background(#ebebe6);
    net.tick(0.5);
    net.draw();
    
    if (!mousePressed && sylCounter!=-1 && sylCounter++ % 10 == 0){
        net.nextSyl();
    }

}


//
// Event handling
//

void mousePressed(){
    SyntaxNet net = (SyntaxNet)songs.elementAt(currentSong);
    selNode = net.hit(mouseX,mouseY);
    println("Click on "+selNode+" started at "+mouseX+","+mouseY);
}


void mouseDragged(){
    if (selNode>=0){
        SyntaxNet net = (SyntaxNet)songs.elementAt(currentSong);
        net.moveNode(selNode,mouseX,mouseY);
    }
}

void mouseReleased(){
    selNode = -1;
}

void keyPressed() {
    if (key == ' '){
        if (sylCounter==-1){ sylCounter = 0; }
        else{ sylCounter = -1; }
    }else if (key == CODED && (keyCode == RIGHT || keyCode == LEFT)){
        SyntaxNet oldNet = (SyntaxNet)songs.elementAt(currentSong);
        oldNet.makeInactive();
        
        if (keyCode == RIGHT){
            currentSong++;
            if (currentSong >= songs.size()){ currentSong = 0; }
        }else if (keyCode == LEFT){
            currentSong--;
            if (currentSong < 0){ currentSong = songs.size()-1; }
        }
        SyntaxNet newNet = (SyntaxNet)songs.elementAt(currentSong);
        newNet.makeActive();
        
    }else if (key == 'c'){
        SyntaxNet net = (SyntaxNet)songs.elementAt(currentSong);
        net.nextSyl();
    }
}

//
// Minim audio init
//

void stop()
{
  Minim.stop();
  super.stop();
}

void resetMinim(){
    Minim.stop();
    Minim.start(this);
}


//
// Birdsong code
//
public class SyntaxNet extends Object
{
    //Smoother3D centroid;
    ParticleSystem physics;
    int activeSyl; // Index of the current syl in the particles array
    int repeatsLeft; // Index of the current repeat (if any)
    int activeRepeat; // Counter to help draw loops around nodes
    String birdName; // Taken from the filename
    String syls; // mapping of indices to syl names (keys for hashtables)
    Hashtable repeats = new Hashtable(); // arrays of probs for self-repeating syls
    Hashtable edges = new Hashtable(); // array of springs to downstream syls
    Hashtable edgeProbs = new Hashtable(); // array of doubles with downstream probs
    Hashtable edgeTargets = new Hashtable(); // array of Strings with downstream syl names
    Hashtable audioSamples = new Hashtable(); // AudioFileIn objects for the syls' .wav files
    Vector history = new Vector();


    SyntaxNet(String jsonFile){
        // expression
        println("Loading "+jsonFile);
        physics = new ParticleSystem( 0.0000001, 0.25 );
        
        
        birdName = jsonFile.substring(0,jsonFile.indexOf("."));
        println("Bird: "+birdName);
        
        // Load in the syntax data
        String synData[] = loadStrings(jsonFile);
        String synText = synData[0];
        try {
            JSONObject synObj = new JSONObject(synText);
            JSONObject sylRepeats = synObj.getJSONObject("repeats");
            JSONArray trans = synObj.getJSONArray("fwd");
            int i,j, numSyls;

            syls = synObj.getString("syls");
            activeSyl = 0;
            repeatsLeft = 0;
            numSyls = syls.length();
            double transMat[] = new double[numSyls*numSyls]; // col: current syl, row: next syl

            // Unpack json data into object instance
            for (i=0; i<numSyls; i++){
                String thisSyl = ""+syls.charAt(i);
                Particle newP = physics.makeParticle(1.0,width/2.0,(height-30-numRows*boxSize)/3.0, 0.0);
                
                for (j=0; j<numSyls; j++){
                    // rotate the matrix here since kgb lied about its orientation
                    transMat[j + numSyls*i] = trans.getDouble(i + numSyls*j);
                }
                
                if (sylRepeats.has(thisSyl)){
                    JSONArray repeatProbs = sylRepeats.getJSONArray(thisSyl);
                    int numProbs = repeatProbs.length();
                    double probArray[] = new double[numProbs];
                    for (j=0; j<numProbs; j++){
                        probArray[j] = repeatProbs.getDouble(j);
                    }
                    repeats.put(thisSyl, probArray);
                    println("Repeats on "+thisSyl+": "+numProbs);
                }
            }


            // Shuffle the particles randomly so they will settle out
            for (i=1; i<numSyls; i++){
                Particle p = physics.getParticle(i-1);
                Particle q = physics.getParticle(i);
                q.moveTo(p.position().x()+random(-4,4), p.position().y()+random(-4,4),0.0);
            }
            
            println ("got "+physics.numberOfParticles()+" syls. transmat len: "+transMat.length);
            
            // Add connections between syls
            for (i=0; i<numSyls; i++){
                
                // first, count up the number of downstream syls
                int numDownstream = 0;
                for (j=0; j<numSyls; j++){
                    if (i==j){continue;}
                    double transProb = transMat[i + numSyls*j];
                    if (transProb>0.05){ numDownstream++; }
                }
                if (numDownstream>0){
                    // Make arrays of downstream springs & probs...
                    int nextIdx = 0;
                    Spring downstream[] = new Spring[numDownstream];
                    double probs[] = new double[numDownstream];
                    String downstreamNames[] = new String[numDownstream];
                    for (j=0; j<numSyls; j++){
                        double transProb = transMat[i + numSyls*j];
                        Particle p_i = physics.getParticle(i);
                        Particle p_j = physics.getParticle(j);
                        if (transProb>0.05){
                            if (i==j){continue;}
                            downstream[nextIdx] = physics.makeSpring( p_i, p_j, EDGE_STRENGTH, EDGE_STRENGTH, (float)(EDGE_LENGTH * (1.0-transProb)) );
                            probs[nextIdx] = transMat[i + numSyls*j];
                            downstreamNames[nextIdx] = ""+syls.charAt(j);
                            nextIdx++;
                        }
                    }
                    
                    // ... and add them to their respective hashtables
                    String sylName = ""+syls.charAt(i);
                    edges.put(sylName,downstream);
                    edgeProbs.put(sylName,probs);
                    edgeTargets.put(sylName,downstreamNames);
                }else{
                    println("No syls downstream from "+syls.charAt(i)+" in song "+jsonFile);
                }

                // Make everything repell everything else
                for (j=0; j<numSyls; j++){
                    if (i==j){continue;}
                    Particle p_i = physics.getParticle(i);
                    Particle p_j = physics.getParticle(j);
                    physics.makeAttraction( p_i, p_j, -SPACER_STRENGTH, 20 );
                }
            
            }
        }catch (JSONException e) {println (e.toString());}
        
    }


    void tick(float dt){
        physics.tick(dt);
        drift();
    }
    

    void drift(){
        
        
        Particle p = physics.getParticle(0);
        float xMin = p.position().x();
        float xMax = xMin;
        float yMin = p.position().y();
        float yMax = yMin;
        
        for (int i=1; i<physics.numberOfParticles(); i++){
            p = physics.getParticle(i);
            xMin = min(xMin,p.position().x());
            xMax = max(xMax,p.position().x());
            yMin = min(yMin,p.position().y());
            yMax = max(yMax,p.position().y());
        }
        
        float leftPadding = xMin - 0;
        float rightPadding = width - xMax;
        float topPadding = yMin - 0;
        float bottomPadding = (height-30-numRows*boxSize) - yMax;
        
        //println();
        //println("l/r padding: "+leftPadding+"/"+rightPadding);
        //println("t/b padding: "+topPadding+"/"+bottomPadding);
        
        
        float xAdjust=0.25;
        float yAdjust=0.25;
        
        if (max(rightPadding,leftPadding)-min(rightPadding,leftPadding) < 10){ xAdjust=0; }
        else if ((rightPadding<leftPadding)){ xAdjust *=-1.; }
        
        if (max(topPadding,bottomPadding) - min(topPadding,bottomPadding) < 10){ yAdjust=0; }
        else if ((topPadding>bottomPadding)){ yAdjust *=-1.; }
        
        for (int i=0; i<syls.length(); i++){
            p = physics.getParticle(i);
            p.moveBy(xAdjust,yAdjust,0);
            physics.tick(0);
        }
    }


    void makeActive(){
        // Load the audio sample for this syllable
        audioSamples.clear();
        
        println("Loading syls for bird "+birdName+": "+syls);
        
        for (int i=0; i<syls.length(); i++){
            //println("trying to load "+birdName+"/"+birdName+"."+syls.charAt(i)+".wav");
            audioSamples.put(""+syls.charAt(i),Minim.loadSample(birdName+"/"+birdName+"."+syls.charAt(i)+".wav"));
            AudioSample snd = (AudioSample)audioSamples.get(""+syls.charAt(i));
        }
        
        
        // select an i/j/k syllable to start with
        if (syls.indexOf("i")!=-1){
            activeSyl = syls.indexOf("i");
        }else if (syls.indexOf("j")!=-1){
            activeSyl = syls.indexOf("j");
        }else if (syls.indexOf("k")!=-1){
            activeSyl = syls.indexOf("k");
        }else{
            activeSyl = 0;
        }

        if (repeats.containsKey(""+syls.charAt(activeSyl))){
            int numRepeats = randomSel((double [])repeats.get(""+syls.charAt(activeSyl)));
            repeatsLeft = numRepeats+1;
            activeRepeat = 0;
        }else{
            repeatsLeft = 0;
            activeRepeat = 0;
        }


    }
    
    void makeInactive(){
        audioSamples.clear();
        resetMinim();
        history.clear();
    }
    
    int hit(float clickX, float clickY){
        float hitRadius = 20.0;
        for (int i=0; i<physics.numberOfParticles(); i++){
            Particle p = physics.getParticle(i);
            float rad = sqrt(pow(p.position().x()-clickX,2)+pow(p.position().y()-clickY,2));
            if (rad<hitRadius){
                activeSyl = i;
                String activeSylName = ""+syls.charAt(activeSyl);
                if (repeats.containsKey(activeSylName)){
                    int numRepeats = randomSel((double [])repeats.get(activeSylName));
                    repeatsLeft = numRepeats+1;
                    activeRepeat = 0;
                    //println("Selected "+activeSylName+" with "+repeatsLeft+" repeats");
                }else{
                    repeatsLeft = 0;
                    activeRepeat = 0;
                }
                
                return i;
            }
        }
        return -1;
    }
    
    void moveNode(int nodeIdx, float toX, float toY){
        println("Moving node "+nodeIdx);
        Particle p = physics.getParticle(nodeIdx);
        p.moveTo(toX,toY,0.0);
    }
    
    
    void nextSyl(){
        String currSyl = ""+syls.charAt(activeSyl);
        if (edgeProbs.containsKey(currSyl)){
            if (repeatsLeft>0){
                // We're in a repeat cycle, see if we continue
                repeatsLeft--;
                activeRepeat++;
                //println(repeatsLeft+" more repeats");
            }else{
                // Roll the dice to decide on a new sylable ...
                int nextEdgeIdx = randomSel((double[])edgeProbs.get(currSyl));
                String possibleTargets[] = (String [])edgeTargets.get(currSyl);
                int nextSylIdx = syls.indexOf(possibleTargets[nextEdgeIdx]);
                activeSyl = nextSylIdx;
                
                // ... and number of repeats
                if (repeats.containsKey(""+syls.charAt(activeSyl))){
                    int numRepeats = randomSel((double [])repeats.get(""+syls.charAt(activeSyl)));
                    repeatsLeft = numRepeats+1;
                    activeRepeat = 0;
                }else{
                    repeatsLeft = 0;
                    activeRepeat = 0;
                }
            }
            AudioSample snd = (AudioSample)audioSamples.get(""+syls.charAt(activeSyl));
            snd.trigger();
            history.addElement(""+syls.charAt(activeSyl));
        }
        
        /*print("Syls:");
        for (int i=0; i<history.size(); i++){
            print(" "+history.elementAt(i));
        }
        println();*/
        
    }

    int randomSel(double rawprobs[]){
        double probs[] = new double[rawprobs.length];
        for (int i=0; i<rawprobs.length; i++){
            probs[i] = rawprobs[i];
        }
        double rawSum = 0.0;
        for (int i=0; i<probs.length; i++){
            rawSum+=probs[i];
        }
        for (int i=0; i<probs.length; i++){
            probs[i]/=rawSum;
            if (i>0){ probs[i]+=probs[i-1];}
            //println("Prob "+i+": "+probs[i]);
        }

        double selection = random(1.0);
        for (int i=0; i<probs.length; i++){
            if (selection<probs[i]){ return i; }
        }
        return probs.length-1;
    }
    
    void draw(){
        int numParticles = physics.numberOfParticles();
        int numSprings = physics.numberOfSprings();

        //Particle currSyl = physics.getParticle(syls.indexOf(activeSyl));
        //println("Active syl is "+activeSyl+" which is particle "+syls.indexOf(activeSyl)+": "+currSyl);
        Particle currSyl = physics.getParticle(activeSyl);

        if (selNode != -1 && mousePressed && (mouseButton == LEFT)) {
            /// BUG: does this make the other click handlers redundant?
            moveNode(selNode, mouseX,mouseY);
        }
        
        // draw repeats
        noStroke();
        for ( int i = 0; i < numParticles; ++i ){
            // draw the dot for the syl
            Particle v = physics.getParticle(i);
            
            // draw rings for repeats (if any)
            String thisSyl = ""+syls.charAt(i);
            if (repeats.containsKey(thisSyl)){
                double repeatProbs[] = (double [])repeats.get(thisSyl);
                //println("Syl "+thisSyl+" has "+repeatProbs.length+" repeats");
                noFill();
                strokeWeight(2);
                float annulusRad = NODE_SIZE+10;
                if (activeSyl==i){ annulusRad+=5; }
                for (int j=0; j<repeatProbs.length; j++){
                    if (activeSyl==i){
                        //stroke(255,255,(int)(255 * (1.0-repeatProbs[j])));
                        //stroke(lerpColor(color(#ff0000),color(#ffffff),.95*(1.0-(float)repeatProbs[j])));
                        stroke(lerpColor(color(#755408),color(#ebebe6),.8*(1.0-(float)repeatProbs[j])));
                    }else{
                        stroke(lerpColor(color(0),color(#ebebe6),.8*(1.0-(float)repeatProbs[j])));
                        //stroke((int)(255 * (1.0-repeatProbs[j])));
                    }
                    ellipse( v.position().x(), v.position().y(), annulusRad, annulusRad);
                    //if (activeSyl==i){println(thisSyl+" rad is "+annulusRad+": "+(int)(255 * (1.0-repeatProbs[j])));}
                    //if (activeSyl==i){println(thisSyl+" rad is "+annulusRad+": "+repeatProbs[j]);}
                    annulusRad+=10;
                }

                // Draw ring showing the current repeat (if any)
                if (activeSyl==i){
                    annulusRad = NODE_SIZE+5;
                    stroke(255,0,0);
                    for (int j=0; j<=activeRepeat; j++){
                        ellipse( v.position().x(), v.position().y(), annulusRad, annulusRad);
                        annulusRad+=10;
                    }
                }

            }
        }

        // draw edges 
        String activeSylName = ""+syls.charAt(activeSyl);
        Enumeration sylKeys = edges.keys();
        while(sylKeys.hasMoreElements()){
            String skey = (String)sylKeys.nextElement();
            Spring springs[] = (Spring[])edges.get(skey);
            double probs[] = (double[])edgeProbs.get(skey);
            for (int i=0; i<springs.length; i++){
                Particle a = springs[i].getOneEnd();
                Particle b = springs[i].getTheOtherEnd();
            
                if (skey.equals(activeSylName)){
                    stroke( #ff0000 );
                    stroke(lerpColor(color(#ff0000),color(#696B56),.95*(1.0-(float)probs[i])));
                    strokeWeight(ceil(8*(float)probs[i]));
                }else{
                    stroke( #696B56 );
                    strokeWeight(ceil(6*(float)probs[i]));
                }
            
                line(a.position().x(), a.position().y(),
                     b.position().x(), b.position().y() );
             }
        }

        // draw syl nodes
        noStroke();
        for ( int i = 0; i < numParticles; ++i ){
            // draw the dot for the syl
            Particle v = physics.getParticle(i);
            String nodeName = ""+syls.charAt(i);
            float thisNodeSize = NODE_SIZE;
            if (v == currSyl){
                fill(#B38513);
                thisNodeSize *= 1.333;
            }else{
                fill(20);
            }
            ellipse( v.position().x(), v.position().y(), thisNodeSize,thisNodeSize);
            fill(255);
            textFont(labelFont,12);
            textAlign(CENTER);
            text(nodeName,v.position().x(), v.position().y()+4);
        }        
        
        
        // draw the syl history
        float cursor[] = {0,height-numRows*boxSize};
        
        // Clip the oldest sylables off the history array so we don't overflow
        while(history.size()>numRows*numCols){
            for (int i=0; i<numCols; i++){history.removeElementAt(0);}
            
        }

        // draw a backdrop, then plot a colored square for each syl
        fill(#D0D0CB);
        rect(0,height-30-numRows*boxSize,width,30+numRows*boxSize);

        for (int i=0; i<history.size(); i++){
            String thisSyl = (String)history.elementAt(i);
            fill(sylPalette[syls.indexOf(thisSyl)]);
            rect(cursor[0],cursor[1],boxSize,boxSize);
            fill(255);

            boolean shouldDraw = true;
            if (i>0){
                String prevSyl = (String)history.elementAt(i-1);
                if (thisSyl.equals(prevSyl)){ shouldDraw = false; }
            }
            
            if (shouldDraw){
                textFont(boxFont);
                textAlign(CENTER);
                text(thisSyl,cursor[0]+boxSize/2,cursor[1]+3*boxSize/4-1);
            }

            cursor[0] += boxSize;
            if (cursor[0]>=width){
                cursor[0] = 0;
                cursor[1] += boxSize;
            }
        }
        
        // label this bird
        fill(60);
        textAlign(LEFT);
        textFont(legendFont,20);
        text("Bird ",10,height-8-numRows*boxSize);
        fill(120);
        text(birdName,10+textWidth("Bird "),height-8-numRows*boxSize);
    }
}
