package com.myapp;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javafx.util.Pair;

public class Day3 {
    static char NOT_SYMBOL = '.';
    public static void main (String [] args) {
        System.out.println("Hello World!");
        part1();
        part2();
    }
    public static void part1() {
        int sum = 0;
        List<String> inputs = Utils.parseInput("day3.txt");
        int cNum = inputs.get(0).length();
        int rNum = inputs.size();
        char [][] a = new char[cNum][rNum];

        for (int r = 0; r < cNum; r++) {
            String s = inputs.get(r);
            for (int c = 0; c < rNum; c++) {
                char ch = s.toCharArray()[c];
                a[r][c] = ch;
            }
        }

        for (int r = 0; r < cNum; r++) {
            for (int c = 0; c < rNum; c++) {
                char ch = a[r][c];
                if (ch == '.') continue;
                if (Character.isDigit(ch)) {
                    String num = "";
                    List<Pair<Integer,Integer>> indexList = new ArrayList<>();
                    while (Character.isDigit(ch)) {
                        Pair<Integer,Integer> index = new Pair<>(r,c);
                        indexList.add(index);
                        num += String.valueOf(ch);
                        c++;
                        if (c >= cNum) break;
                        ch = a[r][c];
                    }
                    //check neighbor
                    if (isAdjecentToSymbol(a, indexList, cNum, rNum)) {
                        sum += Integer.valueOf(num);
                    }
                }
            }
        }
        System.out.println(sum);
    }
    public static boolean isAdjecentToSymbol (char[][]a, List<Pair<Integer,Integer>> indexList,
            int cNum, int rNum) {
        return isAdjecentToSymbol(a, indexList, cNum, rNum, NOT_SYMBOL);
    }

    public static boolean isAdjecentToSymbol (char[][]a, List<Pair<Integer,Integer>> indexList,
            int cNum, int rNum, char symbol) {
        for (Pair<Integer,Integer> index : indexList) {
            for (Pair<Integer,Integer> neighbor : Utils.getAdjecentToSymbolIndex(a, index, true)) {
                if (isSymbol(a, neighbor.getKey(), neighbor.getValue(), cNum, rNum, symbol)) {
                    return true;
                }
            }
        }
        return false;
    }
    public static Pair<Integer,Integer> getAdjecentToSymbolIndex(char[][]a, List<Pair<Integer,Integer>> indexList,
            int cNum, int rNum, char symbol) {
        for (Pair<Integer,Integer> index : indexList) {
            for (Pair<Integer,Integer> neighbor : Utils.getAdjecentToSymbolIndex(a, index, true)) {
                if (isSymbol(a, neighbor.getKey(), neighbor.getValue(), cNum, rNum, symbol)) {
                    return neighbor;
                }
            }
        }
        return null;
    }
    public static boolean isSymbol(char [][]a, int r, int c, int rNum, int cNum) {
        if (r >= 0 && r < rNum && c >= 0 && c < cNum) {
            char ch = a[r][c];
            if (!Character.isDigit(ch) && !Character.isAlphabetic(ch) && ch != '.')
                return true;
        }
        return false;
    }
    public static boolean isSymbol(char [][]a, int r, int c, int rNum, int cNum, char symbol) {
        if (symbol != NOT_SYMBOL) {
            if (r >= 0 && r < rNum && c >= 0 && c < cNum) {
                char ch = a[r][c];
                if (ch == symbol)
                    return true;
            }
        }
        else {
            return isSymbol(a, r, c, rNum, cNum);
        }
        return false;
    }
    public static void part2() {
        int sum = 0;
        List<String> inputs = Utils.parseInput("day3.txt");
        int cNum = inputs.get(0).length();
        int rNum = inputs.size();
        char [][] a = new char[cNum][rNum];

        for (int r = 0; r < cNum; r++) {
            String s = inputs.get(r);
            for (int c = 0; c < rNum; c++) {
                char ch = s.toCharArray()[c];
                a[r][c] = ch;
            }
        }

        Map<Pair<Integer,Integer>, List<String>> gearMap = new HashMap<>();
        for (int r = 0; r < cNum; r++) {
            for (int c = 0; c < rNum; c++) {
                char ch = a[r][c];
                if (ch == '.') continue;
                if (Character.isDigit(ch)) {
                    String num = "";
                    List<Pair<Integer,Integer>> indexList = new ArrayList<>();
                    while (Character.isDigit(ch)) {
                        Pair<Integer,Integer> index = new Pair<>(r,c);
                        indexList.add(index);
                        num += String.valueOf(ch);
                        c++;
                        if (c >= cNum) break;
                        ch = a[r][c];
                    }
                    //check neighbor
                    Pair<Integer,Integer> starIndex = getAdjecentToSymbolIndex(a, indexList, cNum, rNum, '*');
                    if (starIndex != null) {
                        List<String> numAdjList = gearMap.getOrDefault(starIndex, new ArrayList<String>());
                        numAdjList.add(num);
                        gearMap.put(starIndex, numAdjList);
                    }
                }
            }
        }
        for (Pair<Integer,Integer> gear : gearMap.keySet()) {
            List<String> numAdjList = gearMap.get(gear);
            if (numAdjList.size() == 2) {
                sum += Integer.valueOf(numAdjList.get(0)) * Integer.valueOf(numAdjList.get(1));
            }
        }
        System.out.println(sum);
    }
}
