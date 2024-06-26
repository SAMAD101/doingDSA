package Arrays;

public class Leetcode_219 {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 1};
        System.out.println(containsNearbyDuplicate(nums, 3));
    }

    public static boolean containsNearbyDuplicate(int[] nums, int k) {
        for(int i=0; i<nums.length; i++){
            for(int j=i+1; j<i+k+1 && j<nums.length; j++){
                if(nums[i]==nums[j] && (j-i)<=k)
                    return true;
            }
        }
        return false;
    }
}
