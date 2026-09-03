data = {}

while True:
    line = input().strip()
    if line == "end":
        break

    city, temp, rain = line.split()
    temp = float(temp)

    if city not in data:
        data[city] = {"temps": [], "rainy_days": 0}

    data[city]["temps"].append(temp)

    if rain == "yes":
        data[city]["rainy_days"] += 1


results = []
for city, info in data.items():
    avg_temp = sum(info["temps"]) / len(info["temps"])
    results.append((city, avg_temp, info["rainy_days"]))

results.sort(key=lambda x: (-x[2], x[0]))

for city, avg_temp, rainy_days in results:
    temp = f"{avg_temp:.2f}"
    if temp[-1] == "0":
        temp = temp[:-1]
    print(f"{city} {temp} {rainy_days}")