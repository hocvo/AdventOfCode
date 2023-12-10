package com.myapp;

import java.math.BigInteger;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.stream.Collectors;

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
//        int inNum = ins.size();
        // find all steps to Z from any loc
        // DOES NOT NEEDED. Assume always perfect loop. Offset always 0
//        Integer[] insArray = ins.toArray(new Integer[0]);
//        Map<String,Map<Long,Long>> offsetMap = new HashMap<>();
//        for (String loc : map.keySet()) {
//            Map<Long,Long> offsetM = new HashMap<>();
//            for (long i = 0; i < insArray.length; i++) {
//                offsetM.put(i, calculateStep(ins,i,loc,map));
//            }
//            offsetMap.put(loc, offsetM);
//        }
        List<String> locList = map.keySet().stream()
            .filter(loc -> loc.endsWith("A"))
            .collect(Collectors.toList());
        long[] steps = new long[locList.size()];

        for (int i = 0; i < steps.length; i++) {
            String loc = locList.get(i);
            steps[i] = calculateStep(ins, 0, loc, map);
        }

        long result = calculateLCM(steps);
        long stop = System.currentTimeMillis();
        System.out.println(result);
        System.out.println("Time: " + (stop-start));
    }

    static class OffsetMap {
        String loc;
        // off set and the step to Z
        Map<Integer,Integer> map = new HashMap<>();
    }
    static long calculateStep(Queue<Integer> ins, long offset, String loc, Map<String,String[]> map) {
        long step = 0;
        while (offset-- > 0) {
            // put offset back to end of queue
            ins.add(ins.poll());
        }
        while(!ins.isEmpty() && !loc.endsWith("Z")) {
            int instruction = ins.poll();
            loc = map.get(loc)[instruction];
            step++;
            // put back to queue to loop as needed
            ins.add(instruction);
        }
        return step;
    }
    static boolean isFinish(Collection<String> list) {
        return list.stream().allMatch(l -> l.endsWith("Z"));
    }
    static boolean isDone(long[] steps) {
        if (steps[0] == 0) return false;
        return Arrays.stream(steps).distinct().count() == 1;
    }
    static long calculateLCM(long [] steps) {
        long lcm = steps[0];
        for (int i = 1; i < steps.length; i++) {
            lcm = lcm(lcm, steps[i]);
        }
        return lcm;
    }
    static long lcm(long a, long b) {
        BigInteger A = BigInteger.valueOf(a);
        BigInteger B = BigInteger.valueOf(b);
        return a * (b / A.gcd(B).longValue());
    }
}
