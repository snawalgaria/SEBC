# Adjusted values:

Since  Cloudera Manager reserves 20% of RAM for the OS, so I adjusted value of formula in B7 to
=PRODUCT(0,2;B3)
```

# Workload factor

As explained during the lab, that for the cloud clusters workload factor more than 1 is not a good configuration, since the VMs can get crammed leading to the hypervisor killing them, therefore i choose this to be 1
