package com.myapp;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class Day7
{
    static List<Character> CARDS = Arrays.asList('2','3','4','5','6','7','8','9','T','J','Q','K','A');
    static List<Character> CARDS_JOKER = Arrays.asList('J','2','3','4','5','6','7','8','9','T','Q','K','A');
    public static void main (String[] args)
    {
        List<String> inputs = Utils.parseInput("day7.txt");
        part1(inputs);
        part2(inputs);
    }
    enum Type {
        HighCard,
        OnePair,
        TwoPair,
        ThreeKind,
        FullHouse,
        FourKind,
        FiveKind
    }
    static class Hand {
        char [] cards = new char[5];
        int bid;
        Type type = Type.HighCard;
        Hand(String s, int bid) {
            cards = s.toCharArray();
            this.bid = bid;
        }
        Hand(String s, int bid, Type type) {
            cards = s.toCharArray();
            this.bid = bid;
            this.type = type;
        }
    }
    @Deprecated
    static class FiveKind extends Hand {
        FiveKind (String s, int bid)
        {
            super(s, bid);
        }
    }
    @Deprecated
    static class FourKind extends Hand {
        FourKind (String s, int bid)
        {
            super(s, bid);
        }
    }
    @Deprecated
    static class FullHouse extends Hand{
        FullHouse (String s, int bid)
        {
            super(s, bid);
        }
    }
    @Deprecated
    static class ThreeKind extends Hand{
        ThreeKind (String s, int bid)
        {
            super(s, bid);
        }
    }
    @Deprecated
    static class TwoPair extends Hand{
        TwoPair (String s, int bid)
        {
            super(s, bid);
        }
    }
    @Deprecated
    static class OnePair extends Hand{
        OnePair (String s, int bid)
        {
            super(s, bid);
        }
    }
    @Deprecated
    static class HighCard extends Hand{
        HighCard (String s, int bid)
        {
            super(s, bid);
        }
    }

    static Hand createHand(String s, int bid) {
        char[] cards = s.toCharArray();
        int pairCount = 0;
        int maxSimilar = 0;
        Set<Integer> done = new HashSet<>();
        for (int i = 0; i < cards.length; i++) {
            if (done.contains(i)) continue;
            int similarCount = 1; // include its own
            for (int j = i+1; j < cards.length; j++) {
                if (i == j || done.contains(j)) continue;
                if (cards[i] == cards[j]) {
                    similarCount++;
                    done.add(i);
                    done.add(j);
                }
            }
            if (similarCount == 2) pairCount++;
            if (similarCount > 2) maxSimilar = similarCount;
        }
//        System.out.printf("%s: kind: %d, pair: %d\n", s, maxSimilar, pairCount);
        switch(maxSimilar) {
            case 5:
                return new Hand(s, bid, Type.FiveKind);
            case 4:
                return new Hand(s, bid, Type.FourKind);
            case 3:
                if (pairCount > 0) return new Hand(s, bid, Type.FullHouse);
                else return new Hand(s, bid, Type.ThreeKind);
            default:
                if (pairCount == 2) return new Hand(s, bid, Type.TwoPair);
                else if (pairCount == 1) return new Hand(s, bid, Type.OnePair);
                else return new Hand(s, bid, Type.HighCard);
        }
    }
    @Deprecated
    static Hand createHandDeprecated(String s, int bid) {
        char[] cards = s.toCharArray();
        int pairCount = 0;
        int maxSimilar = 0;
        Set<Integer> done = new HashSet<>();
        for (int i = 0; i < cards.length; i++) {
            if (done.contains(i)) continue;
            int similarCount = 1; // include its own
            for (int j = i+1; j < cards.length; j++) {
                if (i == j || done.contains(j)) continue;
                if (cards[i] == cards[j]) {
                    similarCount++;
                    done.add(i);
                    done.add(j);
                }
            }
            if (similarCount == 2) pairCount++;
            if (similarCount > 2) maxSimilar = similarCount;
        }
//        System.out.printf("%s: kind: %d, pair: %d\n", s, maxSimilar, pairCount);
        switch(maxSimilar) {
            case 5:
                return new FiveKind(s, bid);
            case 4:
                return new FourKind(s, bid);
            case 3:
                if (pairCount > 0) return new FullHouse(s, bid);
                else return new ThreeKind(s, bid);
            default:
                if (pairCount == 2) return new TwoPair(s, bid);
                else if (pairCount == 1) return new OnePair(s, bid);
                else return new HighCard(s, bid);
        }
    }
    static Hand createHandWildCard(String s, int bid) {
        char[] cards = s.toCharArray();
        int pairCount = 0;
        int maxSimilar = 0;
        int wildCardCount = 0;
        Set<Integer> done = new HashSet<>();
        for (int i = 0; i < cards.length; i++) {
            if (done.contains(i)) continue;
            if (cards[i] == 'J') {
                wildCardCount++;
                done.add(i);
                continue;
            }
            int similarCount = 1; // include its own
            for (int j = i+1; j < cards.length; j++) {
                if (i == j || done.contains(j)) continue;
                if (cards[i] == cards[j]) {
                    similarCount++;
                    done.add(i);
                    done.add(j);
                }
            }
            if (similarCount == 2) pairCount++;
            if (similarCount > 2) maxSimilar = similarCount;
        }
//        System.out.printf("%s: kind: %d, pair: %d\n", s, maxSimilar, pairCount);
//        switch(maxSimilar) {
//            case 5:
//                return new FiveKind(s, bid);
//            case 4:
//                if (wildCardCount > 0)
//                    return new FiveKind(s, bid);
//                return new FourKind(s, bid);
//            case 3:
//                if (wildCardCount == 2)
//                    return new FiveKind(s, bid);
//                else if (wildCardCount == 1)
//                    return new FourKind(s, bid);
//                if (pairCount > 0) return new FullHouse(s, bid);
//                else return new ThreeKind(s, bid);
//            default:
//                if (pairCount == 2) {
//                    if (wildCardCount > 0)
//                        return new FullHouse(s, bid);
//                    return new TwoPair(s, bid);
//                }
//                else if (pairCount == 1) {
//                    if (wildCardCount > 2) {
//                        return new FiveKind(s, bid);
//                    }
//                    else if (wildCardCount > 1) {
//                        return new FourKind(s, bid);
//                    }
//                    else if (wildCardCount > 0) {
//                        return new ThreeKind(s, bid);
//                    }
//                    return new OnePair(s, bid);
//                }
//                else {
//                    if (wildCardCount > 3) {
//                        return new FiveKind(s, bid);
//                    }
//                    if (wildCardCount > 2) {
//                        return new FourKind(s, bid);
//                    }
//                    else if (wildCardCount > 1) {
//                        return new ThreeKind(s, bid);
//                    }
//                    else if (wildCardCount > 0) {
//                        return new OnePair(s, bid);
//                    }
//                    return new HighCard(s, bid);
//                }
//        }
        switch(maxSimilar) {
            case 5:
                return new Hand(s, bid, Type.FiveKind);
            case 4:
                if (wildCardCount > 0)
                    return new Hand(s, bid, Type.FiveKind);
                return new Hand(s, bid, Type.FourKind);
            case 3:
                if (wildCardCount == 2)
                    return new Hand(s, bid, Type.FiveKind);
                else if (wildCardCount == 1)
                    return new Hand(s, bid, Type.FourKind);
                if (pairCount > 0) return new Hand(s, bid, Type.FullHouse);
                else return new Hand(s, bid, Type.ThreeKind);
            default:
                if (pairCount == 2) {
                    if (wildCardCount > 0)
                        return new Hand(s, bid, Type.FullHouse);
                    return new Hand(s, bid, Type.TwoPair);
                }
                else if (pairCount == 1) {
                    if (wildCardCount > 2) {
                        return new Hand(s, bid, Type.FiveKind);
                    }
                    else if (wildCardCount > 1) {
                        return new Hand(s, bid, Type.FourKind);
                    }
                    else if (wildCardCount > 0) {
                        return new Hand(s, bid, Type.ThreeKind);
                    }
                    return new Hand(s, bid, Type.OnePair);
                }
                else {
                    if (wildCardCount > 3) {
                        return new Hand(s, bid, Type.FiveKind);
                    }
                    if (wildCardCount > 2) {
                        return new Hand(s, bid, Type.FourKind);
                    }
                    else if (wildCardCount > 1) {
                        return new Hand(s, bid, Type.ThreeKind);
                    }
                    else if (wildCardCount > 0) {
                        return new Hand(s, bid, Type.OnePair);
                    }
                    return new Hand(s, bid, Type.HighCard);
                }
        }
    }
    @Deprecated
    public static Comparator<Hand> getComparatorDeprecated(List<Character> cardRanking) {
        return (h1, h2) -> {
            if (h1 instanceof FiveKind) {
                if (h2 instanceof FiveKind) {
                    return compareCard(h1,h2,cardRanking);
                }
                else return 1;
            }
            else if (h1 instanceof FourKind) {
                if (h2 instanceof FiveKind) return -1;
                else if (h2 instanceof FourKind) {
                    return compareCard(h1,h2,cardRanking);
                }
                else return 1;
            }
            else if (h1 instanceof FullHouse) {
                if ((h2 instanceof FiveKind) || 
                    (h2 instanceof FourKind)) return -1;
                else if (h2 instanceof FullHouse) {
                    return compareCard(h1,h2,cardRanking);
                }
                else return 1;
            }
            else if (h1 instanceof ThreeKind) {
                if ((h2 instanceof FiveKind) || 
                    (h2 instanceof FourKind) ||
                    (h2 instanceof FullHouse)) return -1;
                else if (h2 instanceof ThreeKind) {
                    return compareCard(h1,h2,cardRanking);
                }
                else return 1;
            }
            else if (h1 instanceof TwoPair) {
                if ((h2 instanceof FiveKind) || 
                    (h2 instanceof FourKind) ||
                    (h2 instanceof FullHouse) ||
                    (h2 instanceof ThreeKind)) return -1;
                else if (h2 instanceof TwoPair) {
                    return compareCard(h1,h2,cardRanking);
                }
                else return 1;
            }
            else if (h1 instanceof OnePair) {
                if ((h2 instanceof FiveKind) || 
                    (h2 instanceof FourKind) ||
                    (h2 instanceof FullHouse) ||
                    (h2 instanceof ThreeKind) ||
                    (h2 instanceof TwoPair)) return -1;
                else if (h2 instanceof OnePair) {
                    return compareCard(h1,h2,cardRanking);
                }
                else return 1;
            }
            else {
                if ((h2 instanceof FiveKind) || 
                    (h2 instanceof FourKind) ||
                    (h2 instanceof FullHouse) ||
                    (h2 instanceof ThreeKind) ||
                    (h2 instanceof TwoPair) ||
                    (h2 instanceof OnePair)) return -1;
                else return compareCard(h1,h2,cardRanking);
            }
        };
    }
    public static Comparator<Hand> getComparator(List<Character> cardRanking) {
        return (h1, h2) -> {
            int type1 = h1.type.ordinal();
            int type2 = h2.type.ordinal();
            if (type1 == type2)
                return compareCard(h1,h2,cardRanking);
            else
                return type1 - type2;
        };
    }

    public static int compareCard(Hand h1, Hand h2, List<Character> cardRanking) {
        for (int i = 0; i < h1.cards.length; i++) {
            int val1 = cardRanking.indexOf((h1.cards[i]));
            int val2 = cardRanking.indexOf((h2.cards[i]));
            if (val1 > val2) return 1;
            else if (val2 > val1) return -1;
        }
        return 0;
    }
    public static void part1 (List<String> inputs)
    {
        long start = System.currentTimeMillis();
        long sum = 0;
        Set<Hand> in = new TreeSet<>(getComparator(CARDS));
        for (String s : inputs) {
            String [] pair = s.split("\\s+");
            in.add(createHand(pair[0], Integer.parseInt(pair[1])));
        }
        int rank = 1;
        for (Hand h : in) {
            sum += h.bid * rank++;
        }
        long stop = System.currentTimeMillis();
        System.out.println(sum);
        System.out.println("Time: " + (stop-start));
    }

    public static void part2 (List<String> inputs)
    {

        long start = System.currentTimeMillis();
        long sum = 0;
        Set<Hand> in = new TreeSet<>(getComparator(CARDS_JOKER));
        for (String s : inputs) {
            String [] pair = s.split("\\s+");
            in.add(createHandWildCard(pair[0], Integer.parseInt(pair[1])));
        }
        int rank = 1;
        for (Hand h : in) {
            sum += h.bid * rank++;
        }
        long stop = System.currentTimeMillis();
        System.out.println(sum);
        System.out.println("Time: " + (stop-start));
    }

}
