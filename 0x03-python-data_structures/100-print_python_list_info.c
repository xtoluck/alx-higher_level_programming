#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - This is a function that prints some basic
 *							info about [given] Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	int element;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (element = 0; element < Py_SIZE(p); element++)
		printf("Element %d: %s\n", element, Py_TYPE(PyList_GetItem(p, element))->tp_name);
}
