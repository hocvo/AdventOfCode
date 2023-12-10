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

import javafx.util.Pair;

@SuppressWarnings("restriction")
public class Day10
{
    static Set<Pair<Integer,Integer>> loop;
    public static void main (String[] args)
    {
        System.out.println("Hello World!");
        List<String> inputs = Utils.parseInput("test.txt");
        int numRow = inputs.size();
        int numCol = inputs.get(0).length();
        char [][] tiles = new char [numRow][numCol];
        Pair<Integer,Integer> start = null;
        for (int r = 0; r < numRow; r++) {
            String s = inputs.get(r);
            char[] chars = s.toCharArray();
            tiles [r] = chars;
            int startIndex = s.indexOf('S');
            if (start == null && startIndex > -1) {
                start = new Pair<>(r,startIndex);
            }
        }
        int [][] steps = part1(tiles, start);
        part2(tiles, steps, start);
    }

    public static int[][] part1 (char[][] tiles, Pair<Integer,Integer> startIndex)
    {
        long start = System.currentTimeMillis();
        int maxStep = 0;
        Queue<Pair<Integer,Integer>> q = new ArrayDeque<>();
        int[][] steps = new int[tiles.length][tiles[0].length];
        q.add(startIndex);
        Set<Pair<Integer,Integer>> seen = new HashSet<>();
        while(!q.isEmpty()) {
            Pair<Integer,Integer> loc = q.poll();
            if (seen.contains(loc)) continue;
            seen.add(loc);
            int r = loc.getKey();
            int c = loc.getValue();
            int curStep = steps[r][c];
            List<Pair<Integer,Integer>> neighbors = Utils.getAdjecentToIndex2(tiles, loc, false);
            char pipe = tiles[r][c];
            switch (pipe) {
            case 'S':
                for (Pair<Integer,Integer> n : neighbors) {
                    int row = n.getKey();
                    int col = n.getValue();
                    char ch = tiles[row][col];
                    if (ch == '.' || seen.contains(n)) continue;
                    if (ch == 'L' && (row < r || col > c)) continue;
                    if (ch == '7' && (row > r || col < c)) continue;
                    if (ch == 'J' && (row < r || col < c)) continue;
                    if (ch == 'F' && (row > r || col > c)) continue;
                    if (ch == '-' && row != r) continue;
                    if (ch == '|' && col != c) continue;
                    steps[n.getKey()][n.getValue()] = curStep+1;
                    q.add(n);
                }
                break;
            case 'F':
                for (Pair<Integer,Integer> n : neighbors) {
                    int row = n.getKey();
                    int col = n.getValue();
                    char ch = tiles[row][col];
                    if (ch == '.' || seen.contains(n)) continue;
                    if (row < r || col < c) continue;
                    if ((ch == '|' || ch == 'L')
                            && col != c && row != r+1) continue;
                    if ((ch == '-' || ch == '7')
                            && row != r && col != c+1) continue;
                    steps[row][col] = curStep+1;
                    q.add(n);
                    if (maxStep < curStep+1) maxStep = curStep+1;
                }
                break;
            case '7':
                for (Pair<Integer,Integer> n : neighbors) {
                    int row = n.getKey();
                    int col = n.getValue();
                    char ch = tiles[row][col];
                    if (ch == '.' || seen.contains(n)) continue;
                    if (row < r || col > c) continue;
                    if ((ch == '|' || ch == 'J')
                            && col != c && row != r+1) continue;
                    if ((ch == '-' || ch == 'F')
                            && row != r && col != c-1) continue;
                    steps[row][col] = curStep+1;
                    q.add(n);
                    if (maxStep < curStep+1) maxStep = curStep+1;
                }
                break;
            case 'J':
                for (Pair<Integer,Integer> n : neighbors) {
                    int row = n.getKey();
                    int col = n.getValue();
                    char ch = tiles[row][col];
                    if (ch == '.' || seen.contains(n)) continue;
                    if (row > r || col > c) continue;
                    if ((ch == '|' || ch == '7')
                            && col != c && row != r-1) continue;
                    if ((ch == '-' || ch == 'L')
                            && row != r && col != c-1) continue;
                    steps[row][col] = curStep+1;
                    q.add(n);
                    if (maxStep < curStep+1) maxStep = curStep+1;
                }
                break;
            case 'L':
                for (Pair<Integer,Integer> n : neighbors) {
                    int row = n.getKey();
                    int col = n.getValue();
                    char ch = tiles[row][col];
                    if (ch == '.' || seen.contains(n)) continue;
                    if (row > r || col < c) continue;
                    if ((ch == '|' || ch == 'F')
                            && col != c && row != r-1) continue;
                    if ((ch == '-' || ch == 'J')
                            && row != r && col != c+1) continue;
                    steps[row][col] = curStep+1;
                    q.add(n);
                    if (maxStep < curStep+1) maxStep = curStep+1;
                }
                break;
            case '-':
                for (Pair<Integer,Integer> n : neighbors) {
                    int row = n.getKey();
                    int col = n.getValue();
                    char ch = tiles[row][col];
                    if (ch == '.' || seen.contains(n)) continue;
                    if (row != r || ch == '|') continue;
                    steps[row][col] = curStep+1;
                    q.add(n);
                    if (maxStep < curStep+1) maxStep = curStep+1;
                }
                break;
            case '|':
                for (Pair<Integer,Integer> n : neighbors) {
                    int row = n.getKey();
                    int col = n.getValue();
                    char ch = tiles[row][col];
                    if (ch == '.' || seen.contains(n)) continue;
                    if (col != c || ch == '-') continue;
                    steps[row][col] = curStep+1;
                    q.add(n);
                    if (maxStep < curStep+1) maxStep = curStep+1;
                }
                break;
            default:
                // char . for ground
                break;
            }

            for (int[] columns : steps) {
                for (int step : columns) {
                    System.out.printf("%3d",step);
                }
                System.out.println();
            }
            System.out.println();
        }

        long stop = System.currentTimeMillis();
        System.out.println(maxStep);
        System.out.println((stop-start));
        loop = seen;
        return steps;
    }
    public static void part2(char[][] tiles, int[][]steps, Pair<Integer,Integer> startIndex)
    {
        long start = System.currentTimeMillis();
        long sum = 0;
        Queue<Pair<Integer,Integer>> q = new ArrayDeque<>();
        // add all step that's has not process
        for (int i = 0; i < steps.length; i++) {
            for (int j = 0; j < steps[0].length; j++) {
                if (steps[i][j] == 0) q.add(new Pair<>(i,j));
            }
        }
//        steps[startIndex.getKey()][startIndex.getValue()] = -1;
        Set<Pair<Integer,Integer>> seen = new HashSet<>();
        while (!q.isEmpty()) {
            Pair<Integer,Integer> loc = q.poll();
            if (seen.contains(loc)) continue;
            seen.add(loc);
            Queue<Pair<Integer,Integer>> qt = new ArrayDeque<>();
            Set<Pair<Integer,Integer>> connected = new HashSet<>();
            qt.add(loc);
            while (!qt.isEmpty()) {
                if (seen.contains(loc)) continue;
                seen.add(loc);
                boolean isOut = false;
                List<Pair<Integer,Integer>> neighbors = Utils.getAdjecentToIndex2(tiles, loc, false);
                for (Pair<Integer,Integer> n : neighbors) {
                    int row = loc.getKey();
                    int col = loc.getValue();
                    if (!loop.contains(n)) {
                        connected.add(n);
                        qt.add(n);
                    }
                    else if (row == 0 || col == 0) {
                        // hit outer edge, must be outside
                        // reset connected and break
                        isOut = true;
                        break;
                    }
                }
                if (isOut) break;
            }
            sum += connected.size();
        }
        long stop = System.currentTimeMillis();
        System.out.println(sum);
        System.out.println((stop-start));
    }
}
