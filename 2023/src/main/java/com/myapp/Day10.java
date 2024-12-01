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
        List<String> inputs = Utils.parseInput("day10.txt");
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
        part2Visual(tiles, steps, start);
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
            List<Pair<Integer,Integer>> neighbors = Utils.getAdjecentToIndex(tiles, loc, false);
            char pipe = tiles[r][c];
            for (Pair<Integer,Integer> n : neighbors) {
                if (seen.contains(n)) continue;
                int row = n.getKey();
                int col = n.getValue();
                if (isAllowed(pipe, row, col, tiles, r, c)) {
                    steps[n.getKey()][n.getValue()] = curStep+1;
                    q.add(n);
                    maxStep = Math.max(maxStep,curStep+1);
                }
            }
//         
//            for (int[] columns : steps) {
//                for (int step : columns) {
//                    System.out.printf("%3d",step);
//                }
//                System.out.println();
//            }
//            System.out.println();
        }

        long stop = System.currentTimeMillis();
        System.out.println(maxStep);
        System.out.println((stop-start));
        loop = seen;
        return steps;
    }
    public static void part2Visual(char[][] tiles, int[][]steps, Pair<Integer,Integer> startIndex) {
        steps[startIndex.getKey()][startIndex.getValue()] = 1;
        for (int i = 0; i < steps.length; i++) {
            for (int j = 0; j < steps[0].length; j++) {
                if (steps[i][j] > 0) {
                    System.out.print(tiles[i][j]);
                }
                else {
                    System.out.print(0);
                }
                
            }
            System.out.println();
        }
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
        
        // process all tiles that's not a part of the loop
        Set<Pair<Integer,Integer>> seen = new HashSet<>();
        while (!q.isEmpty()) {
            Pair<Integer,Integer> loc = q.poll();
            if (seen.contains(loc)) continue;
            seen.add(loc);
            // for each tile, expand until hit outer edge, or the loop's edges
            Queue<Pair<Integer,Integer>> qt = new ArrayDeque<>();
            Set<Pair<Integer,Integer>> connected = new HashSet<>();
            int connectedNum = 1; // include the processing tile itself
            qt.add(loc);
            while (!qt.isEmpty()) {
                if (seen.contains(loc)) continue;
                seen.add(loc);
                int r = loc.getKey();
                int c = loc.getValue();
                char pipe = tiles[r][c];
                boolean isOut = false;
                List<Pair<Integer,Integer>> neighbors = Utils.getAdjecentToIndex(tiles, loc, false);
                for (Pair<Integer,Integer> n : neighbors) {
                    int row = n.getKey();
                    int col = n.getValue();
                    if (!loop.contains(n)) {
//                        connected.add(n);
                        connectedNum++;
                        qt.add(n);
                    }
                    else if (row == 0 || col == 0
                            || row == tiles.length -1 || col == tiles[0].length) {
                        // hit outer edge, must be outside
                        // reset connected and break
                        isOut = true;
                        connectedNum = 0;
                        break;
                    }
                    else {
                        if (!isIn(pipe, row, col, tiles, r, c)) {
                            isOut = true;
                            break;
                        }
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
    static boolean isAllowed(char pipe, int row, int col,
            char[][] tiles, int r, int c) {
        char ch = tiles[row][col];
        if (ch == '.') return false;
        switch (pipe) {
        case 'S':
            if (ch == 'L' && (row < r || col > c)) return false;
            if (ch == '7' && (row > r || col < c)) return false;
            if (ch == 'J' && (row < r || col < c)) return false;
            if (ch == 'F' && (row > r || col > c)) return false;
            if (ch == '-' && row != r) return false;
            if (ch == '|' && col != c) return false;
            break;
        case 'F':
            if (row < r || col < c) return false;
            if ((ch == '|' || ch == 'L')
                    && col != c && row != r+1) return false;
            if ((ch == '-' || ch == '7')
                    && row != r && col != c+1) return false;
            break;
        case '7':
                if (row < r || col > c) return false;
                if ((ch == '|' || ch == 'J')
                        && col != c && row != r+1) return false;
                if ((ch == '-' || ch == 'F')
                        && row != r && col != c-1) return false;
            break;
        case 'J':
                if (row > r || col > c) return false;
                if ((ch == '|' || ch == '7')
                        && col != c && row != r-1) return false;
                if ((ch == '-' || ch == 'L')
                        && row != r && col != c-1) return false;
            break;
        case 'L':
                if (row > r || col < c) return false;
                if ((ch == '|' || ch == 'F')
                        && col != c && row != r-1) return false;
                if ((ch == '-' || ch == 'J')
                        && row != r && col != c+1) return false;
            break;
        case '-':
                if (row != r || ch == '|') return false;
            break;
        case '|':
                if (col != c || ch == '-') return false;
            break;
        default:
            // char . for ground
            break;
        }
        return true;
    }
    static boolean isIn(char pipe, int row, int col,
            char[][] tiles, int r, int c) {
        char ch = tiles[row][col];
        switch (pipe) {
        case 'F':
            if (row < r || col < c) return false;
            if ((ch == '|' || ch == 'L')
                    && col != c && row != r+1) return false;
            if ((ch == '-' || ch == '7')
                    && row != r && col != c+1) return false;
            break;
        case '7':
                if (row < r || col > c) return false;
                if ((ch == '|' || ch == 'J')
                        && col != c && row != r+1) return false;
                if ((ch == '-' || ch == 'F')
                        && row != r && col != c-1) return false;
            break;
        case 'J':
                if (row > r || col > c) return false;
                if ((ch == '|' || ch == '7')
                        && col != c && row != r-1) return false;
                if ((ch == '-' || ch == 'L')
                        && row != r && col != c-1) return false;
            break;
        case 'L':
                if (row > r || col < c) return false;
                if ((ch == '|' || ch == 'F')
                        && col != c && row != r-1) return false;
                if ((ch == '-' || ch == 'J')
                        && row != r && col != c+1) return false;
            break;
        default:
            // char . for ground
            break;
        }
        return true;
    }
}
