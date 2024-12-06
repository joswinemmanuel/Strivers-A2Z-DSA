class Solution {
  public:
    // Function to count the number of digits in n that evenly divide n
    int evenlyDivides(int n) {
        int count = 0, digit = 0, data = n;
        while(n > 0) {
            digit = n % 10;
            if((digit != 0) && (data % digit == 0)) {
                count++;
            }
            n /= 10;
        }
        return count;
    }
};
