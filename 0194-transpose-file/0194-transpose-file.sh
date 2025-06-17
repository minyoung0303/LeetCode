awk '
{
    for (i = 1; i <= NF; i++) {
        a[i, NR] = $i
        if (NR > max_row) max_row = NR
        if (i > max_col) max_col = i
    }
}
END {
    for (i = 1; i <= max_col; i++) {
        for (j = 1; j <= max_row; j++) {
            printf "%s%s", a[i, j], (j == max_row ? ORS : " ")
        }
    }
}
' file.txt