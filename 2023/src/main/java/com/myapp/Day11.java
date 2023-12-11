package com.myapp;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import javafx.util.Pair;

@SuppressWarnings("restriction")
public class Day11
{
    static Set<Pair<Integer,Integer>> loop;
    public static void main (String[] args)
    {
        System.out.println("Hello World!");
        List<String> inputs = Utils.parseInput("day11.txt");
        int numRow = inputs.size();
        int numCol = inputs.get(0).length();
        List<List<Character>> g = new ArrayList<>();
        Set<Integer> colHasGalaxy = new HashSet<>();
        Set<Integer> rowNeedExpand = new HashSet<>();
        int galCount = 1;
        for (int r = 0; r < numRow; r++) {
            String s = inputs.get(r);
            List<Character> row  = s.chars()
                    .mapToObj(c -> (char)c)
                    .collect(Collectors.toList());
            if (!row.contains('#')) {
//                g.add(new ArrayList<>(row)); part 1
                rowNeedExpand.add(r);
            }
            else {
                // all columns that contains #
                colHasGalaxy.addAll(IntStream.range(0, numRow)
                        .filter(i -> row.get(i) == '#').boxed()
                        .collect(Collectors.toSet()));
            }
            g.add(row);
        }

        // update # of rows after row expansion
//        numRow = g.size();
//        for (int c = numCol-1; c >= 0; c--) {
//            if (colHasGalaxy.contains(c)) continue;
//            for (int r = 0; r < g.size(); r++) {
//                g.get(r).add(c, '.');
//            }
//        }
        Set<Integer> colneedExpand = new HashSet<>();
        for (int c = 0; c < numCol; c++) {
            if (colHasGalaxy.contains(c)) continue;
            colneedExpand.add(c);
        }
        numCol = g.get(0).size();
        String[][] gal = new String[numRow][numCol];
        for (int i = 0; i < numRow; i++) {
            gal[i] = g.get(i).stream()
                    .map(ch -> ch.toString())
                    .collect(Collectors.toList())
                    .toArray(new String[numCol]);
        }
        List<Pair<Integer,Integer>> galIndex = new ArrayList<>();
        for (int r = 0; r < numRow; r++) {
            for (int c = 0; c < numCol; c++) {
                if (gal[r][c].equals("#")) {
                    gal[r][c] = String.valueOf(galCount++);
                    galIndex.add(new Pair<>(r,c));
                }
            }
        }
        galCount--;
        part1(gal, galIndex, galCount, rowNeedExpand, colneedExpand);
        part2(gal, galIndex, galCount, rowNeedExpand, colneedExpand);
    }

    public static void part1 (String [][] galaxies, List<Pair<Integer,Integer>> galIndex,
            int galCount, Set<Integer> rowNeedExpand, Set<Integer> colNeedExpand)
    {
        long start = System.currentTimeMillis();
        long sumStep = 0;
        for (int i = 0; i < galIndex.size()-1; i++) {
            Pair<Integer,Integer> g1 = galIndex.get(i);
            sumStep += findShortestPath(galaxies, g1, galIndex.subList(i+1, galIndex.size()), galCount,
                    rowNeedExpand, colNeedExpand, 2);
        }
//        for (String[] chList : galaxies) {
//            for (String ch : chList) {
//                System.out.printf("%s",ch);
//            }
//            System.out.println();
//        }
        System.out.println();
        long stop = System.currentTimeMillis();
        System.out.println(sumStep);
        System.out.println((stop-start));
    }
    public static void part2(String [][] galaxies, List<Pair<Integer,Integer>> galIndex,
            int galCount, Set<Integer> rowNeedExpand, Set<Integer> colNeedExpand)
    {
        long start = System.currentTimeMillis();
        long sumStep = 0;
        for (int i = 0; i < galIndex.size()-1; i++) {
            Pair<Integer,Integer> g1 = galIndex.get(i);
            sumStep += findShortestPath(galaxies, g1, galIndex.subList(i+1, galIndex.size()), galCount,
                    rowNeedExpand, colNeedExpand, 1000000);
        }
        System.out.println();
        long stop = System.currentTimeMillis();
        System.out.println(sumStep);
        System.out.println((stop-start));
    }
    static long findShortestPath(String [][] galaxies, Pair<Integer,Integer> g1,
            List<Pair<Integer,Integer>> gs, int galCount, Set<Integer> rowNeedExpand, Set<Integer> colNeedExpand, int xpandLen) {
        Queue<Pair<Integer,Integer>> q = new ArrayDeque<>();
        Set<Pair<Integer,Integer>> seen = new HashSet<>();
        long [][] steps = new long[galaxies.length][galaxies[0].length];
        long [] stepsForEachG = new long[galCount+1]; // offset 0 index
        q.add(g1);
        while (!q.isEmpty()) {
            Pair<Integer,Integer> loc = q.poll();
            if (seen.contains(loc)) continue;
            seen.add(loc);
            int r = loc.getKey();
            int c = loc.getValue();
            List<Pair<Integer,Integer>> neighbors = Utils.getAdjecentToIndex(galaxies.length, galaxies[0].length, loc, false);
            for (Pair<Integer,Integer> n : neighbors) {
                int stepNeed = 1;
                if (seen.contains(n)) continue;
                q.add(n);
                if (rowNeedExpand.contains(n.getKey()) && n.getValue() == c) {
                    stepNeed += xpandLen-1;
                }
                if (colNeedExpand.contains(n.getValue()) && n.getKey() == r) {
                    stepNeed += xpandLen-1;
                }
                steps[n.getKey()][n.getValue()] = steps[r][c] + stepNeed;
            }
            if (gs.contains(loc)) {
                stepsForEachG[Integer.parseInt(galaxies[r][c])] = steps[r][c];
            }
        }
        return Arrays.stream(stepsForEachG).sum();
    }
}