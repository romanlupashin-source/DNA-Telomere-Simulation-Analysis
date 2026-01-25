import random

def create_dna_sequence(length, normal_count, mutant_count):
    bases = ['A', 'T', 'C', 'G']
    # 1. Генерируем "мусорную" ДНК
    dna = ''.join(random.choice(bases) for _ in range(length))
    
    # 2. Добавляем НОРМАЛЬНЫЕ теломеры (TTAGGG)
    telomere_seq = "TTAGGG"
    dna = dna + (telomere_seq * normal_count)
    
    # 3. Добавляем МУТИРОВАВШИЕ теломеры (TTATGG) - буква G заменилась на T
    mutation_seq = "TTATGG"
    dna = dna + (mutation_seq * mutant_count)
    
    return dna

# --- ЭКСПЕРИМЕНТ ---

# Создаем ДНК: 1000 букв мусора, 30 нормальных теломер и 15 мутировавших
my_dna = create_dna_sequence(1000, 30, 15)

print(f"Длина ДНК: {len(my_dna)}")

# --- АНАЛИЗ ---

# Шаг 1: Считаем нормальные
target_normal = "TTAGGG"
count_normal = my_dna.count(target_normal)

# Шаг 2: Считаем мутации
target_mutant = "TTATGG"
count_mutant = my_dna.count(target_mutant)

# Шаг 3: Считаем ОБЩУЮ защиту
total_protection = count_normal + count_mutant

print("-" * 30)
print(f"Нормальных участков: {count_normal}")
print(f"Мутировавших участков: {count_mutant}")
print(f"ИТОГО ЗАЩИТА: {total_protection}")

# Оценка
if total_protection > 40:
    print("ВЕРДИКТ: Клетка молодая и сильная 👶")
else:
    print("ВЕРДИКТ: Клетка стареет 👴")# kinetic-energy-harvester-simulation.2
Python scripts for analyzing stem cell aging markers.
