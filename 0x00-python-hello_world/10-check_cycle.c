#include "lists.h"

/**
 * check_cycle- checks if a singly linked list has a cycle in it.
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	const listint_t *current, *_next;

	current = _next = list;
	while (_next != NULL && _next->next != NULL)
	{
		current = current->next;
		_next = _next->next->next;
		if (current == _next)
			return (1);
	}
	return (0);
}
