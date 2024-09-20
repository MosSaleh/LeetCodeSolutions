class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();

        for(int i : nums1){
            set1.add(i);
        }

        for(int i : nums2){
            set2.add(i);
        }

        List<Integer> solution1 = new ArrayList<>(set1);
        solution1.removeAll(set2);

        List<Integer> solution2 = new ArrayList<>(set2);
        solution2.removeAll(set1);

        return List.of(solution1, solution2);
    }
}