from collections import deque
class Module:
    def __init__(self, name, type, outputs):
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == '%':
            self.memory = 'off'
        else:
            self.memory = {}

    def __repr__(self):
        return self.name + "{type=" + self.type + ",outputs=" + ",".join(self.outputs) + ",memory=" + str(self.memory) + "}"

modules = {}
broadcast_targets = []

with open("day_20_input.txt") as input_file:
    sequences = [(i.split("->")[0].strip(), i.split("->")[1].strip()) for i in input_file.read().split("\n")]

print(sequences)

for sequence in sequences:
    if sequence[0] == 'broadcaster':
        broadcast_targets = sequence[1].split(", ")
        print(f"Broadcast targets: {broadcast_targets}")
    else:
        type = sequence[0][0]
        name = sequence[0][1:]
        outputs = sequence[1].split(", ")
        modules[name] = Module(name, type, outputs)
        print(f"Type: {type}")
        print(f"Name: {name}")
        print(f"Outputs: {outputs}")

# print(f"Modules: {modules}")

# Fill the & memory
for name, module in modules.items():
    print(f"Name: {name}")
    for output in module.outputs:
        print(f"Name: {name} Output: {output}")
        if output in modules and modules[output].type == "&":
            modules[output].memory[name] = 'lo'

print(f"Modules: {modules}")

lo = 0
hi = 0

for n in range(1000):
    # Button pushed lo to broadcaster
    lo += 1
    # Store tuple (origin, target, pulse)
    q = deque([("broadcaster", x, "lo") for x in broadcast_targets])

    while q:
        origin, target, pulse = q.popleft()
        print(f"origin, target, pulse {origin, target, pulse}")
        if pulse == 'lo':
            lo += 1
        else:
            hi += 1

        if target not in modules:
            continue

        module = modules[target]

        # Flipflop %
        if module.type == "%":
            # If hi do nothing, if lo, flip off if on and reverse
            if pulse == 'lo':
                if module.memory == 'off':
                    module.memory = 'on'
                    outgoing = 'hi'
                else:
                    module.memory = 'off'
                    outgoing = 'lo'
                for x in module.outputs:
                    q.append((module.name, x, outgoing))
                    print((module.name, x, outgoing))
        # Conjuction &
        else:
            module.memory[origin] = pulse
            for x in module.memory.values():
                if x == "hi":
                    outgoing = "lo"
                else:
                    outgoing = "hi"
            for x in module.outputs:
                module.memory[origin] = pulse
                print(f"Module memory: {module.memory}")
                if all(x == 'hi' for x in module.memory.values()):
                    outgoing = 'lo'
                    print(f"All hi, outgoing = {outgoing}")
                else:
                    outgoing = 'hi'
                    print(f"Not all hi, outgoing = {outgoing}")
                q.append((module.name, x, outgoing))


print(f"Lo: {lo}, Hi: {hi}, Product of lo and hi {lo * hi}")