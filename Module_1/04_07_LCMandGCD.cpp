class Solution {
  public:
    vector<int> lcmAndGcd(int a, int b) {
        
        int gcd;
        vector<int> result;
        int product = a * b;
        
        while(a>0 && b>0) {
            if(a > b) {
                a = a % b;
            } else {
                b = b % a;
            }
        }
        
        if(a == 0) {
            gcd = b;
        } else {
            gcd = a;
        }
        
        result.push_back(product/gcd);
        result.push_back(gcd);
        
        return result;
    }
};
