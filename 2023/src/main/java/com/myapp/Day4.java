package com.myapp;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Day4 {
    public static void main (String [] args) {
        System.out.println("Hello World!");
        part1();
        part2();
    }
    public static void part1() {
        int sum = 0;
        List<String> inputs = Utils.parseInput("day4.txt");
        for (int i = 0; i < inputs.size(); i++) {
            String s = inputs.get(i).split(":")[1];
            String winNums = s.split("\\|")[0].trim();
            String myNums = s.split("\\|")[1].trim();
            int pts = 0;
            Set<String> winNumSet = new HashSet<>();
            for (String n : winNums.split("\\s+")) {
                if (n.trim() != "")
                    winNumSet.add(n.trim());
            }
            String[] myNum = myNums.split("\\s+");
            for (String num : myNum) {
                String n = num.trim();
                if (n == "") continue;
                if (winNumSet.contains(n)) {
                    if (pts == 0) pts++;
                    else pts *= 2;
                }
            }
            sum += pts;
        }
        System.out.println(sum);
    }

    public static void part2() {
        int sum = 0;
        List<String> inputs = Utils.parseInput("day4.txt");
        int [] instances = new int[inputs.size()+1];
        for (int i = 0; i < inputs.size(); i++) {
            int cardID = i+1;
            instances[cardID]++;
            String s = inputs.get(i).split(":")[1];
            String winNums = s.split("\\|")[0].trim();
            String myNums = s.split("\\|")[1].trim();
            int pts = 0;
            Set<String> winNumSet = new HashSet<>();
            for (String n : winNums.split("\\s+")) {
                if (n.trim() != "")
                    winNumSet.add(n.trim());
            }
            String[] myNum = myNums.split("\\s+");
            for (String num : myNum) {
                String n = num.trim();
                if (n == "") continue;
                if (winNumSet.contains(n)) {
                    pts++;
                    instances[cardID+pts] += instances[cardID];
                }
            }
        }
        for (int i : instances) {
            sum += i;
        }
        System.out.println(sum);
    }
}
