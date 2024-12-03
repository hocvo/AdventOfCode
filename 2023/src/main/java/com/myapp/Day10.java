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
	public static final char[] EXTENDED = { 0x00, 0x00C7, 0x00FC, 0x00E9, 0x00E2,
            0x00E4, 0x00E0, 0x00E5, 0x00E7, 0x00EA, 0x00EB, 0x00E8, 0x00EF,
            0x00EE, 0x00EC, 0x00C4, 0x00C5, 0x00C9, 0x00E6, 0x00C6, 0x00F4,
            0x00F6, 0x00F2, 0x00FB, 0x00F9, 0x00FF, 0x00D6, 0x00DC, 0x00A2,
            0x00A3, 0x00A5, 0x20A7, 0x0192, 0x00E1, 0x00ED, 0x00F3, 0x00FA,
            0x00F1, 0x00D1, 0x00AA, 0x00BA, 0x00BF, 0x2310, 0x00AC, 0x00BD,
            0x00BC, 0x00A1, 0x00AB, 0x00BB, 0x2591, 0x2592, 0x2593, 0x2502,
            0x2524, 0x2561, 0x2562, 0x2556, 0x2555, 0x2563, 0x2551, 0x2557,
            0x255D, 0x255C, 0x255B, 0x2510, 0x2514, 0x2534, 0x252C, 0x251C,
            0x2500, 0x253C, 0x255E, 0x255F, 0x255A, 0x2554, 0x2569, 0x2566,
            0x2560, 0x2550, 0x256C, 0x2567, 0x2568, 0x2564, 0x2565, 0x2559,
            0x2558, 0x2552, 0x2553, 0x256B, 0x256A, 0x2518, 0x250C, 0x2588,
            0x2584, 0x258C, 0x2590, 0x2580, 0x03B1, 0x00DF, 0x0393, 0x03C0,
            0x03A3, 0x03C3, 0x00B5, 0x03C4, 0x03A6, 0x0398, 0x03A9, 0x03B4,
            0x221E, 0x03C6, 0x03B5, 0x2229, 0x2261, 0x00B1, 0x2265, 0x2264,
            0x2320, 0x2321, 0x00F7, 0x2248, 0x00B0, 0x2219, 0x00B7, 0x221A,
            0x207F, 0x00B2, 0x25A0, 0x00A0 };
	public static final String ANSI_RED_BACKGROUND = "\u001B[41m";
    public static final String ANSI_RED = "\u001B[31m";
    public static final String ANSI_CYAN = "\u001B[36m";
    public static final String ANSI_RESET = "\u001B[0m";

    public static final char getAscii(int code) {
        if (code >= 0x80 && code <= 0xFF) {
            return EXTENDED[code - 0x7F];
        }
        return (char) code;
    }
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
//        for (int i=60; i<99; i++) {
//        	System.out.printf("%c%n",EXTENDED[i]);
//        }
        System.out.printf("%c%n",getAscii(191));
        System.out.printf("%c%n",getAscii(192));
        System.out.printf("%c%n",getAscii(217));
        System.out.printf("%c%n",getAscii(218));
        int [][] steps = part1(tiles, start);
//        part2(tiles, steps, start);
        part2Visual(tiles, steps, start);
    }
    static void part2Visual (char[][] tiles, int[][] steps, Pair<Integer,Integer> startIndex) {
    	steps[startIndex.getKey()][startIndex.getValue()] = 1;
    	for (int i = 0; i < tiles.length; i++) {
    		for (int j = 0; j < tiles[i].length; j++) {
    			if (steps[i][j] > 0) {
    				if (tiles[i][j] == 'F') {
    					tiles[i][j] = getAscii(218);
    				}
    				if (tiles[i][j] == 'J') {
    					tiles[i][j] = getAscii(217);
    				}
    				if (tiles[i][j] == '7') {
    					tiles[i][j] = getAscii(191);
    				}
    				if (tiles[i][j] == 'L') {
    					tiles[i][j] = getAscii(192);
    				}
    				if (tiles[i][j] == '-') {
    					tiles[i][j] = getAscii(196);
    				}
    				if (tiles[i][j] == '|') {
    					tiles[i][j] = getAscii(179);
    				}
    				if (i == startIndex.getKey() && j == startIndex.getValue()) {
    					System.out.print(ANSI_CYAN +tiles[i][j]+ANSI_RESET);
    				}
    				else {
    					System.out.print(ANSI_RED+tiles[i][j]+ANSI_RESET);
    				}
    				
    			}
    			else {
    				System.out.print(0);
    			}
    		}
    		System.out.println();
    	}
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
