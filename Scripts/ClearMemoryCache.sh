# Check memory usage
MEMORY=$(free | grep Mem | awk '{print $4/$2 * 100.0}')

# Print memory usage
echo $MEMORY

# Clearing memory cache if memory usage is more than 90%. Clearing page cache, dentries, and inodes
if (( $(echo "$MEMORY > 90.0" | bc -l) )); then
    sync 
    echo 1 > /proc/sys/vm/drop_caches
    echo 2 > /proc/sys/vm/drop_caches
    echo 3 > /proc/sys/vm/drop_caches
    
    echo "Cache memory cleared."
else
    echo "Memory usage is below 90%. No action taken."
fi
