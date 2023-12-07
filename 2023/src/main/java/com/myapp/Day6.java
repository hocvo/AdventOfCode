package com.myapp;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import javafx.util.Pair;

public class Day6
{
    //Time:        41     96     88     94
//    Distance:   214   1789   1127   1055
    static String[] day6 = {"41968894,214178911271055"};
    static String[] test = {"71530,940200"};
    public static long minHold = Long.MAX_VALUE;
    public static long maxHold = 0;
    public static void main (String[] args)
    {
        System.out.println("Hello World!");
        List<Pair<Long,Long>> in = Arrays.asList(day6).stream()
            .map(s
               -> new Pair<>(Long.parseLong(s.split(",")[0]), Long.parseLong(s.split(",")[1])))
            .collect(Collectors.toList());
        part1(in);
        part2(in);
    }

    public static void part1 (List<Pair<Long,Long>> in)
    {
        long start = System.currentTimeMillis();
        long mult = 1;
        for (Pair<Long,Long> p : in) {
            int winCount = 0;
            long time = p.getKey();
            long dist = p.getValue();
            boolean isWinning = false;
            for (long hold = 1; hold < time; hold++) {
                long spd = hold;
                long timeRemain = time - hold;
                long distTmp = spd * timeRemain;
                if (distTmp > dist) {
                    if (!isWinning) {
                        isWinning = true;
                        System.out.println("Min: " + hold);
                    }
                    winCount++;
                }
                else {
                    if (isWinning) {
                        isWinning = false;
                        System.out.println("Max: " + (hold-1));
                        break;
                    }
                }
            }
            mult *= winCount;
        }
        long stop = System.currentTimeMillis();
        System.out.println(mult);
        System.out.println((stop-start));
    }

    public static long hybridSearch(long time, long dist, boolean isSearchMin) {
        long hold = time/2;
        boolean isFound = false;
        boolean isFindingBackward = false;
        while (hold > 1 && hold <= time ) {
            long distTmp = hold * (time-hold); // spd = hold.
            if (distTmp > dist) {
                if (isFindingBackward) return hold;
                isFound = true;
                hold = isSearchMin? hold/2 : hold+(time-hold)/2; // keep cut or increase in half until go out of zone
            } else { // reverse search direction
                if (isFound) {
                    isFindingBackward = true;
                    if (isSearchMin) hold++;
                    else hold--;
                }
            }
        }
        return isSearchMin? Long.MAX_VALUE : 0;
    }
    public static long binarySearchBFS(long time, long dist, boolean isSearchMin) {
        long result = 0;
        boolean isFound = false;
        long min = 1;
        long max = time;
        while (min < max) {
            long hold = (long) Math.floor(min + (max - min)/2);
            long distTmp = hold * (time-hold); // spd = hold.
            if (distTmp > dist) {
                isFound = true;
                if (isSearchMin) {
                    max = hold;
                }
                else {
                    min = hold+1;
                }
                result = hold;
            } else { // reverse search direction
                if (isFound) {
                    if (isSearchMin) {
                        min = hold+1;
                    }
                    else {
                        max = hold;
                    }
                }
            }
        }
        return result;
    }
    public static void binarySearch(long time, long dist, long min, long max, boolean isSearchMin) {
        long hold = (long) Math.floor(min + (max - min)/2);
        if (hold <= 0 || hold >= time) return;
        long timeRemain = time - hold;
        long distTmp = hold * timeRemain;
        if (distTmp > dist) {
            if (hold < minHold) minHold = hold;
            if (hold > maxHold) maxHold = hold;
            if (min >= max) return;
            if (isSearchMin) binarySearch(time, dist, min, hold, true);
            else binarySearch(time, dist, hold+1, max, false);
        }
        else { // reverse search direction
            if (isSearchMin) binarySearch(time, dist, hold+1, max, true);
            else binarySearch(time, dist, min, hold-1, false);
        }
    }
    public static void part2 (List<Pair<Long,Long>> in)
    {
        long start = System.currentTimeMillis();
        long mult = 1;
        for (Pair<Long,Long> p : in) {
            long time = p.getKey();
            long dist = p.getValue();
            minHold = hybridSearch(time, dist, true); // 6-8s
            maxHold = hybridSearch(time, dist, false); // 6-8s
//            binarySearch(time, dist, 1, time, false); // stack overflow
//            binarySearch(time, dist, 1, time, true); // stack overflow. should have known better!
//            minHold = binarySearchBFS(time, dist, true); // best time 0-1s
//            maxHold = binarySearchBFS(time, dist, false); // best time 0-1s
//            System.out.printf("Min: %d, Max: %d\n", minHold, maxHold);
            mult *= maxHold-minHold+1;
        }
        long stop = System.currentTimeMillis();
        System.out.println(mult);
        System.out.println((stop-start));
    }
}
