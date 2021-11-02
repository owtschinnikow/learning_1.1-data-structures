"""
Sample Input:
1 0
Sample Output:


Sample Input:
1 1
0 0
Sample Output:
0

Sample Input:
1 2
0 1
0 1
Sample Output:
0
-1

Sample Input:
1 2
0 1
1 1
Sample Output:
0
1

"""


from collections import deque


def simulating_network_packet_processing(size, number, packets):
    """
    Симулирует работу обработчика пакетов

    >>> simulating_network_packet_processing(2, 5, [[2, 9], [4, 8], [10, 9], [15, 2], [19, 1]])
    2
    11
    -1
    19
    21

    >>> simulating_network_packet_processing(1, 5, [[999999, 1], [1000000, 0], [1000000, 1], [1000000, 0], [1000000, 0]])
    999999
    1000000
    1000000
    -1
    -1
    >>> simulating_network_packet_processing(1, 0, [])

    >>> simulating_network_packet_processing(1, 1, [[0, 0]])
    0
    >>> simulating_network_packet_processing(1, 1, [[0, 1]])
    0
    """
    if packets == []:
        return

    time_arriv = 0
    time_start = 0
    time_process = 0
    time_end = 0

    queue = deque()

    for n in range(number):

        if len(queue) != 0:
            m = 0
            for i in queue:
                # print(i[2], packets[n][0], '\n')
                if i[2] <= packets[n][0]:
                    m += 1
                break

            for i in range(m):
                queue.popleft()

        if len(queue) + 1 > size:
            print('-1')

        elif len(queue) + 1 <= size:
            #определение времени ПРИБЫТИЯ пакета
            time_arriv = packets[n][0]

            # определение времени СТАРТА пакета
            if time_end <= time_arriv:
                time_start = time_arriv
            else:
                time_start = time_end

            # определение времени ПРОЦЕССА пакета
            time_process = packets[n][1]

            # определение времени ОКОНЧАНИЯ пакета
            time_end = time_start + time_process

            # Добавление в очередь полного покета.
            queue.append([n, time_start, time_end])

            # Вывод времени начала пакета

            print(time_start)
            # print(queue)



    return


def main():
    size, number = map(int, input().split())
    packets = [list(map(int, input().split())) for i in range(number)]
    simulating_network_packet_processing(size, number, packets)


if __name__ == '__main__':
    import doctest
    doctest.testmod()#verbose=True
    main()