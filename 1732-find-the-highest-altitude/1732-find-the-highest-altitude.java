class Solution {
    public int largestAltitude(int[] gain) {
        int n = gain.length;
        int[] altitudes = new int[n+ 1];
        altitudes[0] = 0;


        //initialize altitude array
        for(int i = 0; i < n; i++){
            altitudes[i + 1] = gain[i] + altitudes[i];
        }


        // find highest altitude
        return Arrays.stream(altitudes)
            .max()
            .orElse(0);

    }
}