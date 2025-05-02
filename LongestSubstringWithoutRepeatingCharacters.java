class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int maxLength = 0;
        int left = 0;
        java.util.HashSet<Character> seen = new java.util.HashSet<>();

        for (int right = 0; right < n; right++) {
            char currentChar = s.charAt(right);
            while (seen.contains(currentChar)) {
                seen.remove(s.charAt(left));
                left++;
            }
            seen.add(currentChar);
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}
