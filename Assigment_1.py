{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Assigment_1.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPp+AcLyBWecvnIA9RnO5cF"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "ORew--w9pv9z",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 139
        },
        "outputId": "5cf3e830-7e8d-49f6-f5c0-62cc2ca73c8d"
      },
      "source": [
        "# 1) Program to identify a number divisible 7 and not a multiple of 5\n",
        "m = []\n",
        "for i in (range(2000, 3201, 1)):\n",
        "    if (i % 7 == 0) and (i % 5 != 0):\n",
        "        m.append(i)\n",
        "print (m)\n",
        "\n",
        "# 2) Accept user Firstname and Lastname and print in reverse order\n",
        "UserName = []\n",
        "FirstName = str(input(\"Please enter your First name with single quotes : \"))\n",
        "LastName = str(input(\"Please enter your Last name with single quotes : \"))\n",
        "\n",
        "UserName.append(FirstName)\n",
        "UserName.append(LastName)\n",
        "\n",
        "RevUserName = []\n",
        "for i in UserName[::-1]:\n",
        "    RevUserName.append(i)\n",
        "\n",
        "print(FirstName[::-1] + \" \" + LastName[::-1])\n",
        "print(UserName[1] + \" \" + UserName[0])\n",
        "\n",
        "# 3) Program to find vol of sphere with diameter 12\n",
        "SpDiameter = 12\n",
        "pi = 22/7\n",
        "\n",
        "Vol_of_Sp = (4/3) * pi * ((SpDiameter/2) ** 3)\n",
        "\n",
        "print (\"Volume of square with diameter 12 : \", Vol_of_Sp)\n"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[2002, 2009, 2016, 2023, 2037, 2044, 2051, 2058, 2072, 2079, 2086, 2093, 2107, 2114, 2121, 2128, 2142, 2149, 2156, 2163, 2177, 2184, 2191, 2198, 2212, 2219, 2226, 2233, 2247, 2254, 2261, 2268, 2282, 2289, 2296, 2303, 2317, 2324, 2331, 2338, 2352, 2359, 2366, 2373, 2387, 2394, 2401, 2408, 2422, 2429, 2436, 2443, 2457, 2464, 2471, 2478, 2492, 2499, 2506, 2513, 2527, 2534, 2541, 2548, 2562, 2569, 2576, 2583, 2597, 2604, 2611, 2618, 2632, 2639, 2646, 2653, 2667, 2674, 2681, 2688, 2702, 2709, 2716, 2723, 2737, 2744, 2751, 2758, 2772, 2779, 2786, 2793, 2807, 2814, 2821, 2828, 2842, 2849, 2856, 2863, 2877, 2884, 2891, 2898, 2912, 2919, 2926, 2933, 2947, 2954, 2961, 2968, 2982, 2989, 2996, 3003, 3017, 3024, 3031, 3038, 3052, 3059, 3066, 3073, 3087, 3094, 3101, 3108, 3122, 3129, 3136, 3143, 3157, 3164, 3171, 3178, 3192, 3199]\n",
            "Please enter your First name with single quotes : joan\n",
            "Please enter your Last name with single quotes : sal\n",
            "naoj las\n",
            "sal joan\n",
            "Volume of square with diameter 12 :  905.142857142857\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}