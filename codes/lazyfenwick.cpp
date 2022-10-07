void update(int bitType, int idx, int diff) {
    int* bit = bitType==1 ? bit1 : bit2;
    while (idx <= n) {
        bit[idx] += diff;
        idx += idx&-idx;
    }
}

void rangeUpdate(int a, int b, int diff) {
    update(1, a, diff);
    update(1, b+1, -diff);
    update(2, a, diff * (a-1));
    update(2, b+1, -diff * b);
}

int getBitValue(int bitType, int idx) {
    int* bit = bitType==1 ? bit1 : bit2;
    int answer = 0;
    while (idx > 0) {
        answer += bit[idx];
        idx -= idx&-idx;
    }
    return answer;
}

int prefixSum(int idx) {
    return getBitValue(1, idx) * idx - getBitValue(2, idx);
}

int query(int a, int b) {
    return prefixSum(b) - prefixSum(a-1);
}