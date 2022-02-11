int SegmentedSieve(int low, int high) {  // returns the number of primes within range [low, high] inclusive
    int lim = sqrt(high);
    bool ck[lim+1]; memset(ck, true, sizeof(ck));
    vector<int> prime;
    ck[1] = ck[0] = false;
    for (int i = 2; i <= lim; i++) {
        if (ck[i]) {
            prime.push_back(i);
            for (int j = i*i; j <= lim; j += i) ck[j] = false;
        }
    }
    bool isPrime[high-low+1]; memset(isPrime, true, sizeof(isPrime));
    for (int i : prime) {
        for (int j = max(i*i, (low+i-1)/ i*i); j < high; j += i) isPrime[j - low] = false;
    }
    if (low == 1) isPrime[0] = false;
    int ans = 0;
    for (int i = 0; i < high-low; i++) ans += isPrime[i];
    return ans;
}
