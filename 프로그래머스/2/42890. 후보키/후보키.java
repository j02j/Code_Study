//구해야 하는 것 : 후보키 최대 개수
// Set, Hashset : 집합

import java.util.*;

class Solution {
    public int solution(String[][] relation) {
        int rowSize = relation.length;
        int colSize = relation[0].length;
        List<Integer> candidates = new ArrayList<>();

        for (int i = 1; i < (1 << colSize); i++) {
            if (isUnique(relation, i) && isMinimal(candidates, i)) {
                candidates.add(i);
            }
        }

        return candidates.size();
    }

    private boolean isUnique(String[][] relation, int bitset) {
        Set<String> set = new HashSet<>();
        for (String[] tuple : relation) {
            StringBuilder key = new StringBuilder();
            for (int i = 0; i < tuple.length; i++) {
                if ((bitset & (1 << i)) != 0) {
                    key.append(tuple[i]).append(",");
                }
            }
            if (!set.add(key.toString())) return false;
        }
        return true;
    }

    private boolean isMinimal(List<Integer> candidates, int bitset) {
        for (int candidate : candidates) {
            if ((candidate & bitset) == candidate) return false;
        }
        return true;
    }
}