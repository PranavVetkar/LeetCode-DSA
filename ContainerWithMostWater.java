class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxCap = 0;

        while (left < right) {
            int width = right - left;
            int cap = Math.min(height[left], height[right]) * width;
            maxCap = Math.max(maxCap, cap);

            if (height[left] < height[right]) {
                left++;
            } 
            else {
                right--;
            }
        }

        return maxCap;
    }
}