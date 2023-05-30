# plug-late-sr

Retry plugging PBDs to specific SRs on boot, then start VMs which couldn't autostart due to the unreachable SRs.

## Configuration

Create a new file: `/etc/plug-late-sr.ini`.

Then you can use this template to plug a specific SR at boot:

```
[SR_UUID]
# Properties with default values, you can modify these fields
# but it's purely optional. Uncomment them for that.
# pbd-plug-retry-delay=30
# auto-poweron-vms=true
```

Replace the `SR_UUID` flag by your own SR UUID.

Note: if you want to protect many SRs, you can add another `[SR_UUID]` line with specific params.
For example:

```
[7c56d251-9877-48d7-9d0e-6ddd368d2eea]
# Use default properties.

[e986b1a1-9e18-49a1-820b-d0c310bbefa0]
pbd-plug-retry-delay=10
```
