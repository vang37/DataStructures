#Question:
#
#Python allows negative integers to be used as indices into a sequence, 
# such as a string. If string "s" has length "n," and expression "s[k]" 
# is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such 
# that "s[j]" references the same element?
#
#Suppose:   0,  1    ,  2    , ... , n - 2, n - 1 for j,  0 <= j < n;
#And that: -n,  1 - n,  2 - n, ... ,    -2,    -1 for k, -n <= k < 0;
#
#Therefore: j - k = n, j = n + k.
