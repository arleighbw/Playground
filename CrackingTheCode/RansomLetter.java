/*
100 50
zahk dp apdz clo e dk awfvf osb qr sa cqjq zgr nvxtb abjy axa ili wdyw soqku buwcl qcub sautu ii vkrzl bdob nona al zg ombzc c dbun f xkuo lsax hfki j dfft uce ugj ywz vucgg xq udrkt ypy tmxgc ty gar kty dc bznj pzzx clo apdz nvxtb clo sa clo zahk awfvf soqku udrkt udrkt e ypy xkuo tmxgc ombzc wdyw al axa lsax clo abjy osb apdz bdob pzzx zahk c bznj gar osb xkuo zahk zg uce zg clo e apdz gar xq dbun buwcl ili bznj clo osb dc dbun ywz
buwcl qr axa ypy zahk nvxtb dp hfki ii uce dc zg dbun ypy ty cqjq zg kty bznj zg zahk dp c al ugj ywz qcub ywz wdyw hfki gar e axa dp qr kty bznj clo ty vucgg qcub al vkrzl qcub j awfvf soqku lsax bdob nvxtb

returns yes
expected output no

FIXED !!.. need to use loop counters entered and not the actual text elements that exist.. lame, would rather use for each loops.
*/

import java.util.*;

public class RansomLetter {
    private Map<String, Integer> magazineMap;
    //Map<String, Integer> noteMap;
    private String[] noteArr;
    private int magWordCount, noteWordCount;
    
    public RansomLetter(String magazine, String note, int magWordCount, int noteWordCount) {
        magazineMap = new HashMap<String, Integer>();
        
        String[] magLetters = magazine.replaceAll(" ","").split("");
        noteArr = note.replaceAll(" ","").split("");
        this.magWordCount = magWordCount;
        this.noteWordCount = noteWordCount;
        
        for (String magLetter : magLetters) {
            if (magazineMap.containsKey(magLetter)) {
                magazineMap.put(magLetter.trim(), (magazineMap.get(magLetter) + 1));
            }
            else magazineMap.put(magLetter, 1);
        }
        
        //for (int i = 0; i < magWordCount; i++) {
        //    if (magazineMap.containsKey(magLetters[i])) {
        //        magazineMap.put(magLetters[i].trim(), magazineMap.get(magLetters[i]) + 1);
        //    }
        //}
    }
    
    public boolean solve() {        
        for (String sL : noteArr) {
            if (magazineMap.containsKey(sL)) {
           	    if (magazineMap.get(sL) > 1)   magazineMap.put(sL,  magazineMap.get(sL) - 1);
                else                           magazineMap.remove(sL);
            } 
            else return false;
        }
        //for (int i = 0; i < this.noteWordCount; i++) {
        //    if (magazineMap.containsKey(noteArr[i])) {
    	//        if (magazineMap.get(noteArr[i]) > 1) magazineMap.put(noteArr[i], magazineMap.get(noteArr[i]) - 1);
    	//        else magazineMap.remove(noteArr[i]);
        //    }
        //    else return false;
        //}
        
        return true;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        
        // Eat whitespace to beginning of next line
        scanner.nextLine();
        
        RansomLetter s = new RansomLetter(scanner.nextLine(), scanner.nextLine(), m, n);
        scanner.close();
        
        boolean answer = s.solve();
        if(answer)
            System.out.println("Yes");
        else System.out.println("No");
      
    }
}
