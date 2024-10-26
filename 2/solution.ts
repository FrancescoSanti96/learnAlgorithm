function sum(n: number): number {
    if (n === 0) {
        return 0;
    } else {
        return n + sum(n - 1);
    }
}


