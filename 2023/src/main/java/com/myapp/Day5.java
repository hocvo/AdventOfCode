package com.myapp;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.stream.Collectors;

import javafx.util.Pair;

public class Day5
{
    static List<MapData> seedToSoil = new ArrayList<>();
    static List<MapData> soilToFertilizer = new ArrayList<>();
    static List<MapData> fertilizerToWater = new ArrayList<>();
    static List<MapData> waterToLight = new ArrayList<>();
    static List<MapData> lightToTemp = new ArrayList<>();
    static List<MapData> tempToHumid = new ArrayList<>();
    static List<MapData> humidToLoc = new ArrayList<>();
    static List<Long> seeds = null;

    public static class MapData {
        public long dest;
        public long src;
        public long range;
        public MapData(long dest, long src, long range) {
            this.dest = dest;
            this.src = src;
            this.range = range;
        }
    }
    public static void main (String[] args)
    {
        System.out.println("Hello World!");
        List<String> inputs = Utils.parseInput("day5.txt");
        for (int i = 0; i < inputs.size(); i++)
        {
            String line = inputs.get(i);
            if (line.contains("seeds:")) {
                String seedString = inputs.get(i).split(":\\s+")[1];
    
                seeds = Arrays.asList(seedString.split("\\s+"))
                .stream()
                .mapToLong(s -> Long.valueOf(s)).boxed()
                    .collect(Collectors.toList());
            }
            else if (line.contains("seed-to-soil")) {
                i = parseMapData(line, inputs, i, seedToSoil);
            }
            else if (line.contains("soil-to-fertilizer")) {
                i = parseMapData(line, inputs, i, soilToFertilizer);
            }
            else if (line.contains("fertilizer-to-water")) {
                i = parseMapData(line, inputs, i, fertilizerToWater);
            }
            else if (line.contains("water-to-light")) {
                i = parseMapData(line, inputs, i, waterToLight);
            }
            else if (line.contains("light-to-temperature")) {
                i = parseMapData(line, inputs, i, lightToTemp);
            }
            else if (line.contains("temperature-to-humidity")) {
                i = parseMapData(line, inputs, i, tempToHumid);
            }
            else if (line.contains("humidity-to-location")) {
                i = parseMapData(line, inputs, i, humidToLoc);
            }
        }
        part1();
        part2();
    }

    public static void part1 ()
    {
        
        long min = Long.MAX_VALUE;
        for (long seed : seeds)
        {
            long soil = getMapping(seedToSoil, seed);
            long fert = getMapping(soilToFertilizer, soil);
            long water = getMapping(fertilizerToWater, fert);
            long light = getMapping(waterToLight, water);
            long temp = getMapping(lightToTemp, light);
            long humid = getMapping(tempToHumid, temp);
            long loc = getMapping(humidToLoc, humid);
            if (loc < min) min = loc;
        }
        System.out.println(min);
    }

    public static long getMapping(List<MapData> map, long input) {
        long temp = input;
        for (MapData d : map) {
            if (input >= d.src && input <= d.src+d.range-1) {
                temp = input-d.src + d.dest;
            }
        }
        return temp;
    }

    public static int parseMapData(String mapName, List<String> inputs, int i, List<MapData> map) {
        i++;
        while (i < inputs.size() && !inputs.get(i).isEmpty()) {
            String line = inputs.get(i);
            String [] data = line.split("\\s+");
            long dest = Long.parseLong(data[0]);
            long src = Long.parseLong(data[1]);
            long range = Long.parseLong(data[2]);
            map.add(new MapData(dest,src,range));
            i++;
        }
        return i;
    }
    public static void part2 ()
    {
        Set<Pair<Long,Long>> seedPair = new HashSet<>();
        for (int i = 0; i < seeds.size()-1; i +=2) {
            seedPair.add(new Pair<>(seeds.get(i), seeds.get(i) + seeds.get(i+1)-1));
        }
        long min = Long.MAX_VALUE;
        Set<Pair<Long,Long>> soil = getMappingBound(seedToSoil, seedPair);
        Set<Pair<Long,Long>> fert = getMappingBound(soilToFertilizer, soil);
        Set<Pair<Long,Long>> water = getMappingBound(fertilizerToWater, fert);
        Set<Pair<Long,Long>> light = getMappingBound(waterToLight, water);
        Set<Pair<Long,Long>> temp = getMappingBound(lightToTemp, light);
        Set<Pair<Long,Long>> humid = getMappingBound(tempToHumid, temp);
        Set<Pair<Long,Long>> loc = getMappingBound(humidToLoc, humid);
        for (Pair<Long,Long> l : loc ) {
            if (l.getKey() < min) min = l.getKey();
        }
        System.out.println(min);
    }
    public static Set<Pair<Long,Long>> getMappingBound(List<MapData> map, Set<Pair<Long,Long>> inputs) {
        Set<Pair<Long,Long>> res = new HashSet<>();
        Queue<Pair<Long,Long>> q = new ArrayDeque<>();
        q.addAll(inputs);
        for (MapData d : map) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
//            for (Pair<Long,Long> input : inputs) {
                Pair<Long,Long> input = q.poll();
                long min = input.getKey();
                long max = input.getValue();
                long minSrc = d.src;
                long maxSrc = d.src + d.range-1;
                if (min < minSrc && max < minSrc) { // all outside left
                    Pair<Long,Long> tmp = new Pair<>(min, max);
                    q.offer(tmp);
                    continue;
                }
                else if (min < minSrc && max >= minSrc) {
                    Pair<Long,Long> tmp = new Pair<>(min, minSrc-1); // partial outside left
                    q.offer(tmp);
                    if (max > minSrc && max <= maxSrc) { // the part that is inside
                        Pair<Long,Long> tmp2 = new Pair<>(d.dest, d.dest + max - minSrc);
                        res.add(tmp2);
                        continue;
                    }
                    else { 
                        Pair<Long,Long> tmp2 = new Pair<>(d.dest, d.dest+d.range-1); // part that's inside
                        res.add(tmp2);
                        Pair<Long,Long> tmp3 = new Pair<>(maxSrc+1, max);// partial outside right
                        q.offer(tmp3);
                    }
                }
                else if (min >= minSrc && max <= maxSrc) { // all inside
                    Pair<Long,Long> tmp2 = new Pair<>(d.dest + min - minSrc, d.dest + max - minSrc);
                    res.add(tmp2);
                    continue;
                }
                else if (min >= minSrc && min <= maxSrc && max > maxSrc) {
                    // part that's inside toward right
                    Pair<Long,Long> tmp = new Pair<>(d.dest + min - minSrc, d.dest+ d.range-1);
                    res.add(tmp);
                    // part that's outside right
                    Pair<Long,Long> tmp2 = new Pair<>(maxSrc+1, max);
                    q.offer(tmp2);
                }
                else if (min > maxSrc) {
                    Pair<Long,Long> tmp = new Pair<>(min, max);
                    q.add(tmp);
                }
            }
        }
        res.addAll(q);
        // merge segments. Doesn't needed (if everything else work correctly)
//        List<Pair<Long,Long>> sorted = res.stream()
//            .sorted(Comparator.comparingLong(l->l.getKey()))
//            .collect(Collectors.toList());
//        Set<Pair<Long,Long>> clean = new HashSet<>();
//        for (int i = 0; i < sorted.size(); i++) {
//            long min = sorted.get(i).getKey();
//            long max = sorted.get(i).getValue();
//            if (i == sorted.size() -1) clean.add(new Pair<>(min,max));
//            for (int j = i+1; j < sorted.size(); j++) {
//                long nextMin = sorted.get(j).getKey();
//                long nextMax = sorted.get(j).getValue();
//                if (max >= nextMin && max <= nextMax) {
//                    max = nextMax;
//                    i = j;
//                    if (i >= sorted.size()-1)
//                        clean.add(new Pair<>(min,max));
//                }
//                else if (max > nextMax) continue;
//                else {
//                    clean.add(new Pair<>(min,max));
//                    break;
//                }
//            }
//        }
//        return clean;
        return res;
    }
}
