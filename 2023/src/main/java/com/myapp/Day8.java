package com.myapp;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Collection;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;
import java.util.TreeSet;
import java.util.function.ToIntFunction;
import java.util.stream.Collectors;

import javafx.util.Pair;

public class Day8
{
    public static void main (String[] args)
    {
        List<String> inputs = Utils.parseInput("day8.txt");
        Queue<Integer> ins = new ArrayDeque<>();
        ins.addAll(inputs.get(0)
            .chars()
            .mapToObj(i -> (i=='L')? 0:1)
            .collect(Collectors.toList()));
        Map<String,String[]> map = new HashMap<>();
        for (String line : inputs.subList(2, inputs.size())) {
            String[] locs = line.split(" = ");
            String loc = locs[0].trim();
            String[] nextLocs = locs[1].replaceAll("\\(","").replaceAll("\\)","").split(", ");
            map.put(loc, nextLocs);
        }
//        part1(ins, map);
        part2(ins, map);
    }
    public static void part1 (Queue<Integer> ins, Map<String,String[]> map)
    {
        long start = System.currentTimeMillis();
        long step = 0;
        String loc = "AAA";
        while(!ins.isEmpty() && !loc.equals("ZZZ")) {
            int instruction = ins.poll();
            loc = map.get(loc)[instruction];
            step++;
            // put back to queue to loop as needed
            ins.add(instruction);
        }
        long stop = System.currentTimeMillis();
        System.out.println(step);
        System.out.println("Time: " + (stop-start));
    }

    public static void part2 (Queue<Integer> ins, Map<String,String[]> map)
    {

        long start = System.currentTimeMillis();
        long step = 0;
        Set<String> locList = map.keySet().stream()
            .filter(loc -> loc.endsWith("A"))
            .collect(Collectors.toSet());
        Set<String> endLocList = map.keySet().stream()
            .filter(loc -> loc.endsWith("Z"))
            .collect(Collectors.toSet());
        locList.addAll(endLocList);
        int insLen = ins.size();
        //TODO Cache the result every step
        Map<String,Set<Long>> cache = new HashMap<>();
        for (String loc : locList) {
            if (cache.containsKey(loc)) {
                continue;
            }
            for (String zLoc : endLocList) {
                Set<String> seenAgainAtIndex = new HashSet<>();
                boolean isFound = true;
                long stepTmp = 0;
                String tmpLoc = loc;
                int i = 0;
                while(!tmpLoc.equals(zLoc)) {
//                    if (seen.contains(tmpLoc)) {
//                        isFound = false;
//                        break; // fall in to infinite loop
//                    }
                    seenAgainAtIndex.add(tmpLoc);
                    int instruction = ins.poll();
                    stepTmp++;
                    tmpLoc = map.get(tmpLoc)[instruction];
                    // put back to queue to loop as needed
                    ins.add(instruction);
                    i++;
                }
                if (isFound) {
                    Set<Long> steps = cache.getOrDefault(loc, new HashSet<>());
                    steps.add(stepTmp);
                    cache.put(loc, steps);
                }
            }
        }
        long stop = System.currentTimeMillis();
        System.out.println(step);
        System.out.println("Time: " + (stop-start));
    }

    static boolean isFinish(Collection<String> list) {
        return list.stream().allMatch(l -> l.endsWith("Z"));
    }
}
