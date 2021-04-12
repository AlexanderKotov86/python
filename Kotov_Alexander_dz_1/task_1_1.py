seconds_count = int(input('Укажите время в секундах: '))
years = (60 * 60 * 24 * 7 * 4 * 12)
months = (60 * 60 * 24 * 7 * 4)
weeks = (60 * 60 * 24 * 7)
days = (60 * 60 * 24)
hours = (60 * 60)
minutes = 60
seconds = 1

total_counts = [years, months, weeks, days, hours, minutes, seconds]
total_counts_print = ["y", "mth", "wk", "d", "h", "min", "sec"]
idx = 0

while idx < len(total_counts):
    if seconds_count >= total_counts[idx]:
        counter = seconds_count // total_counts[idx]
        print(counter, total_counts_print[idx], end=" ")
        seconds_count = seconds_count % total_counts[idx]
        idx = idx + 1
    else:
        print(0, total_counts_print[idx], end=" ")
        idx = idx + 1
