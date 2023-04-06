import pandas as pd
import numpy as np

from scipy.stats import erlang


chat_id = 477096063 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = x.size
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return 2 / 23**2 * (loc + erlang.ppf(alpha / 2, n, loc=0, scale=1/n) - 1/2) , \
           2 / 23**2 * (loc - 1/2 + erlang.ppf(1 - alpha / 2, n, loc=0, scale=1/n))

