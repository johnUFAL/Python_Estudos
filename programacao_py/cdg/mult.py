def maior(nums):
    maior_num = nums[0]
    for n in nums:
        if n > maior_num:
            maior_num = n
    return maior_num

def menor(nums):
    menor_num = nums[0]
    for n in nums:
        if n < menor_num:
            menor_num = n
    return menor_num 

def media(nums):
    soma = 0
    tam = len(nums)
    for n in nums:
        soma += n
    return soma / tam

def main():
    nums = [1, 3, 203, 203, 12, 394, 2993]
    print(f"A lista é: {nums}")

    print(f"O maior valor é: {maior(nums)}")
    print(f"O menor valor é: {menor(nums)}")
    print(f"A média é: {media(nums):.2f}")

if __name__ == '__main__':
    main()