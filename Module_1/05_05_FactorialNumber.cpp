class Solution {
  public:
    vector<long long> factorialNumbers(long long n) {
        // Write Your Code here
        vector<long long> result;
        long long int f = 1;
        int x = 2;
        while(f <= n) {
            result.push_back(f);
            f *= x;
            x++;
        }
        return result;
    }
};
