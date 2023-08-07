#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	/*
	 * declaring pointers to list
	 * both pointers point to the head
	 */
	listint_t *head1 = list;
	listint_t *head2 = list;

	/* validate parameters */
	if (!list)
	{
		return (0);
	} /* end if */

	/*
	 * iterating through the nodes
	 */
	while (head1 && head2 && head2->next)
	{
		head1 = head1->next;
		head2 = head2->next->next;

		/* head2 will catch up with head1 if there is a cycle */
		if (head1 == head2)
		{
			return (1);
		} /* end if */
	} /* end while */

	return (0);
} /* end function */
