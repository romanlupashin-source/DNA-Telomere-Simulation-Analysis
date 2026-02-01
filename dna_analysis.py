import random

def create_dna_sequence(length: int, normal_count: int, mutant_count: int) -> str:
    """
    Generate a synthetic DNA sequence with normal and mutated telomere regions.
    """
    bases = ['A', 'T', 'C', 'G']

    # 1. Generate background DNA (noise)
    dna = ''.join(random.choice(bases) for _ in range(length))

    # 2. Add normal telomeres (TTAGGG)
    normal_telomere = "TTAGGG"
    dna += normal_telomere * normal_count

    # 3. Add mutated telomeres (TTATGG)
    mutant_telomere = "TTATGG"
    dna += mutant_telomere * mutant_count

    return dna


def analyze_telomeres(dna: str) -> None:
    """
    Analyze telomere integrity and aging markers.
    """
    target_normal = "TTAGGG"
    target_mutant = "TTATGG"

    count_normal = dna.count(target_normal)
    count_mutant = dna.count(target_mutant)

    total_protection = count_normal + count_mutant

    print("-" * 40)
    print(f"Normal telomeres detected: {count_normal}")
    print(f"Mutated telomeres detected: {count_mutant}")
    print(f"Total telomere protection score: {total_protection}")

    if total_protection > 40:
        print("Verdict: Cell is biologically young and stable 🧬")
    else:
        print("Verdict: Signs of cellular aging detected ⚠️")


if __name__ == "__main__":
    # Experimental parameters
    dna_sample = create_dna_sequence(
        length=1000,
        normal_count=30,
        mutant_count=15
    )

    print(f"DNA sequence length: {len(dna_sample)}")
    analyze_telomeres(dna_sample)
