class Solution {
    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) return new ArrayList<>();
        String[] mappings = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        List<String> result = new ArrayList<>();
        result.add("");
        for (char digit : digits.toCharArray()) {
            String letters = mappings[digit - '2'];
            List<String> tempResult = new ArrayList<>();
            for (String combination : result) {
                for (char letter : letters.toCharArray()) {
                    tempResult.add(combination + letter);
                }
            }
            result = tempResult;
        }
        return result;
    }
}