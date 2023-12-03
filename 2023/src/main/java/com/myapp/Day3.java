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
            //top left
            Pair<Integer,Integer> tl = new Pair<>(index.getKey()-1,index.getValue()-1);
            if (isSymbol(a, tl.getKey(), tl.getValue(), cNum, rNum, symbol)) {
                return true;
            }
            //top
            Pair<Integer,Integer> t = new Pair<>(index.getKey()-1,index.getValue());
            if (isSymbol(a, t.getKey(), t.getValue(), cNum, rNum, symbol)) {
                return true;
            }
            //top right
            Pair<Integer,Integer> tr = new Pair<>(index.getKey()-1,index.getValue()+1);
            if (isSymbol(a, tr.getKey(), tr.getValue(), cNum, rNum, symbol)) {
                return true;
            }
            //right
            Pair<Integer,Integer> r = new Pair<>(index.getKey(),index.getValue()+1);
            if (isSymbol(a, r.getKey(), r.getValue(), cNum, rNum, symbol)) {
                return true;
            }
            //bottom right
            Pair<Integer,Integer> br = new Pair<>(index.getKey()+1,index.getValue()+1);
            if (isSymbol(a, br.getKey(), br.getValue(), cNum, rNum, symbol)) {
                return true;
            }
            //bottom
            Pair<Integer,Integer> b = new Pair<>(index.getKey()+1,index.getValue());
            if (isSymbol(a, b.getKey(), b.getValue(), cNum, rNum, symbol)) {
                return true;
            }
            //bottom left
            Pair<Integer,Integer> bl = new Pair<>(index.getKey()+1,index.getValue()-1);
            if (isSymbol(a, bl.getKey(), bl.getValue(), cNum, rNum, symbol)) {
                return true;
            }
            //left
            Pair<Integer,Integer> l = new Pair<>(index.getKey(),index.getValue()-1);
            if (isSymbol(a, l.getKey(), l.getValue(), cNum, rNum, symbol)) {
                return true;
            }
        }
        return false;
    }
    public static Pair<Integer,Integer> getAdjecentToSymbolIndex(char[][]a, List<Pair<Integer,Integer>> indexList,
            int cNum, int rNum, char symbol) {
        for (Pair<Integer,Integer> index : indexList) {
            //top left
            Pair<Integer,Integer> tl = new Pair<>(index.getKey()-1,index.getValue()-1);
            if (isSymbol(a, tl.getKey(), tl.getValue(), cNum, rNum, symbol)) {
                return tl;
            }
            //top
            Pair<Integer,Integer> t = new Pair<>(index.getKey()-1,index.getValue());
            if (isSymbol(a, t.getKey(), t.getValue(), cNum, rNum, symbol)) {
                return t;
            }
            //top right
            Pair<Integer,Integer> tr = new Pair<>(index.getKey()-1,index.getValue()+1);
            if (isSymbol(a, tr.getKey(), tr.getValue(), cNum, rNum, symbol)) {
                return tr;
            }
            //right
            Pair<Integer,Integer> r = new Pair<>(index.getKey(),index.getValue()+1);
            if (isSymbol(a, r.getKey(), r.getValue(), cNum, rNum, symbol)) {
                return r;
            }
            //bottom right
            Pair<Integer,Integer> br = new Pair<>(index.getKey()+1,index.getValue()+1);
            if (isSymbol(a, br.getKey(), br.getValue(), cNum, rNum, symbol)) {
                return br;
            }
            //bottom
            Pair<Integer,Integer> b = new Pair<>(index.getKey()+1,index.getValue());
            if (isSymbol(a, b.getKey(), b.getValue(), cNum, rNum, symbol)) {
                return b;
            }
            //bottom left
            Pair<Integer,Integer> bl = new Pair<>(index.getKey()+1,index.getValue()-1);
            if (isSymbol(a, bl.getKey(), bl.getValue(), cNum, rNum, symbol)) {
                return bl;
            }
            //left
            Pair<Integer,Integer> l = new Pair<>(index.getKey(),index.getValue()-1);
            if (isSymbol(a, l.getKey(), l.getValue(), cNum, rNum, symbol)) {
                return l;
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
