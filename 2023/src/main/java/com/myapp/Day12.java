package com.myapp;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import javafx.util.Pair;

@SuppressWarnings("restriction")
public class Day12
{
    static Set<Pair<Integer,Integer>> loop;
    public static void main (String[] args)
    {
        System.out.println("Hello World!");
        List<String> inputs = Utils.parseInput("day12.txt");
        List<Pair<String,String>> in = inputs.stream()
                .map(s -> new Pair<String,String>(s.split("\\s")[0],s.split("\\s")[1]))
                .collect(Collectors.toList());
//        char[] test = {'.','#','#','#','.','#','.','#','.','#','.','.'};
//        int [] test2 = {3,2,1};
//        System.out.println(quickCheck(test,test2));
        part1(in);
//        part2(in);
    }

    public static void part1 (List<Pair<String,String>> in)
    {
        long start = System.currentTimeMillis();
        long sum = 0;
        
        for (Pair<String,String> p : in) {
            String tmp = p.getKey();
            char[] puzzle = tmp.toCharArray();
            int[] expect = Arrays.stream(p.getValue().split(","))
                    .mapToInt(s->Integer.parseInt(s))
                    .toArray();
            Set<String> seen = new HashSet<>();
            sum += dfsBruteForce(Arrays.copyOf(puzzle, puzzle.length), expect, seen);
        }
        long stop = System.currentTimeMillis();
        System.out.println("result: " + sum);
        System.out.println((stop-start));
    }
    public static void part2 (List<Pair<String,String>> in)
    {
        long start = System.currentTimeMillis();
        long sum = 0;
        
        for (Pair<String,String> p : in) {
            String tmp = p.getKey();
            String pTmp = "?" + tmp;
            for (int i = 0; i < 5; i++) {
                tmp += pTmp;
            }
            char[] puzzle = tmp.toCharArray();
            int[] etmp = Arrays.stream(p.getValue().split(","))
                    .mapToInt(s->Integer.parseInt(s))
                    .toArray();
            int[] expect = new int[etmp.length*5];
            for (int i = 0; i < expect.length; i++) {
                expect[i] = etmp[i%etmp.length];
            }
            Set<String> seen = new HashSet<>();
            sum += dfsBruteForce(Arrays.copyOf(puzzle, puzzle.length), expect, seen);
        }
        long stop = System.currentTimeMillis();
        System.out.println("result: " + sum);
        System.out.println((stop-start));
    }
    static int dfsBruteForce(char[] p, int[] expected, Set<String> seen) {
        int sum = 0;
        sum += isMatched(Arrays.copyOf(p, p.length) , 0, '#', expected, seen);
        sum += isMatched(Arrays.copyOf(p, p.length) , 0, '.', expected, seen);
        return sum;
    }
    static int isMatched(char[] p, int i, char val, int[] expected, Set<String> seen) {
        int sum = 0;
        if (i >= p.length) {
            String s = new String(p);
            if (seen.contains(s)) return sum;
            seen.add(s);
            if (isMatched(p, expected))
                sum++;
            return sum;
        }
        if (!quickCheck(p, expected)) {
            return sum;
        }
        if (p[i] == '?') {
            p[i] = '#';
            sum += isMatched(Arrays.copyOf(p, p.length) , i+1, '#', expected, seen);
            p[i] = '.';
            sum += isMatched(Arrays.copyOf(p, p.length) , i+1, '.', expected, seen);
        }
        return sum + isMatched(Arrays.copyOf(p, p.length) , i+1, val, expected, seen);
    }
    static boolean quickCheck(char[]p, int[] expected) {
        String str = new String(p);
        List<String> groups = Arrays.asList(str.split("\\.+"));
        groups = groups.stream()
                .filter(s -> !s.isEmpty())
                .collect(Collectors.toList());
        for (int i = 0; i < expected.length && i < groups.size(); i++) {
            String grp = groups.get(i);
            if (grp.contains("?")) return true; // still in work. let it pass
            long tagCount = grp.chars()
                    .filter(c -> c == '#')
                    .count();
            if (tagCount != expected[i])
                return false;
        }
        return true;
    }
    static boolean isMatched(char[] p, int[] expected) {
        int i = 0;
        boolean allMatched = true;
        for (int expectedCount : expected) {
            boolean matched = false;
            int count = 0;
            while (i < p.length) {
                if (p[i] == '#') {
                    count++;
                    if (i == p.length-1 && count == expectedCount) {
                        matched = true;
                    }
                }
                else {
                    if (count > 0) {
                        if (count == expectedCount)
                            matched = true;
                        break;
                    }
                }
                i++;
            }
            allMatched = allMatched & matched;
            if (allMatched == false) break;
        }
        for (int j = i; j < p.length; j++) {
            if (p[j] == '#') return false;
        }
        return allMatched;
    }
}