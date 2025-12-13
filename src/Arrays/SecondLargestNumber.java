package Arrays;

import java.util.Arrays;

public class SecondLargestNumber {
    public static void main(String [] args){
        int [] nums = {2,99,0,-1,-90,-899};
        System.out.println(secondLargest(nums));
    }

    /*
    Brute Force
    Time Complexity: O(nlogn)
    Space Complexity: O(1)
     */
    public static int secondLargest(int [] nums){
        Arrays.sort(nums);
        int largest = nums[nums.length-1];
        for(int i = nums.length-2; i >= 0; i--){
                if(largest != nums[i]){
                    return nums[i];
            }
        }return -1;
    }
}
