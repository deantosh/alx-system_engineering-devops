/*
 * Author: Deantosh Daiddoh
 * File: 0-linear.c
 */

#include "search_algos.h"

/**
 * linear_search - Searches for a value in an arry of integers using
 *		the lineaar search algorithm.
 * @array: A pointer to the first element of the array to search.
 * @size: The size of the array.
 * @value: The value to search for.
 *
 * Return: first index of value (success) or -1 (fails).
 */
int linear_search(int *array, size_t size, int value)
{
	int *curr = array;
	size_t i = 0;

	/*if array is null or size is 0*/
	if (!array || size == 0)
		return (-1);

	for (i = 0; i < size; i++)
	{
		/*print value checked*/
		printf("Value checked array[%ld] = [%d]\n", i, *curr);
		if (*curr == value)
			return (i);
		/*move ptr*/
		curr++;
	}
	/*if value not found*/
	return (-1);
}
