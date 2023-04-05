import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 477096063 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = x.size
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return 2 / 23**2 * (loc + gamma.ppf(alpha / 2, a=1) - 1/2) , \
           2 / 23**2 * (loc - 1/2 + gamma.ppf(1 - alpha / 2, a=1))

