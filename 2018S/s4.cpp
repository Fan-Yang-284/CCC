#include <bits/stdc++.h>

using namespace std;
long int getTrees(long int weight);
map <long int, long int> dp; //memo

int main(){
    long int N;
    cin>>N;
    long int half = floor(N/2);
    long int res = N-half;
    
    for(long int i = half;i>1;i--){
        res+=getTrees(floor(N/i));
    }
    cout<<res;
}

long int getTrees(long int weight){
        if(weight<=2){return 1;}
        if(dp.find(weight) != dp.end()){
            return dp[weight];
        }
        long int half1 = floor(weight/2);
        long int ans = weight - half1;
        for(long int i = half1;i>1;i--){
            ans+=getTrees(floor(weight/i));
        }
        dp[weight] = ans;
        return ans;
    }