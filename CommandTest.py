import hebi, time

lookup = hebi.Lookup()
group = lookup.get_group_from_names(['Nimbus'], ['Arm_M3'])
cmd = hebi.GroupCommand(group.size)
fbk = hebi.GroupFeedback(group.size)

# Get initial position
group.get_next_feedback(reuse_fbk=fbk)
zero_pos = fbk.position[0]

target = zero_pos + 0.5

# Send continuously for 5 seconds
start = time.time()
while time.time() - start < 5.0:
    cmd.position = [target]
    group.send_command(cmd)
    time.sleep(0.01)  # 100 Hz loop

