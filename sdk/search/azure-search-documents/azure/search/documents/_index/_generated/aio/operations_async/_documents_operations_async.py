# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6246, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class DocumentsOperations:
    """DocumentsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~search_index_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def count(
        self,
        request_options: Optional["models.RequestOptions"] = None,
        **kwargs
    ) -> int:
        """Queries the number of documents in the index.

        :param request_options: Parameter group.
        :type request_options: ~search_index_client.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: long or the result of cls(response)
        :rtype: long
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[int]
        error_map = kwargs.pop('error_map', {})
        
        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2019-05-06-Preview"

        # Construct URL
        url = self.count.metadata['url']
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'indexName': self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.SearchErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('long', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    count.metadata = {'url': '/docs/$count'}

    async def search_get(
        self,
        search_text: Optional[str] = None,
        search_options: Optional["models.SearchOptions"] = None,
        request_options: Optional["models.RequestOptions"] = None,
        **kwargs
    ) -> "models.SearchDocumentsResult":
        """Searches for documents in the index.

        :param search_text: A full-text search query expression; Use "*" or omit this parameter to
         match all documents.
        :type search_text: str
        :param search_options: Parameter group.
        :type search_options: ~search_index_client.models.SearchOptions
        :param request_options: Parameter group.
        :type request_options: ~search_index_client.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchDocumentsResult or the result of cls(response)
        :rtype: ~search_index_client.models.SearchDocumentsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SearchDocumentsResult"]
        error_map = kwargs.pop('error_map', {})
        
        _include_total_result_count = None
        _facets = None
        _filter = None
        _highlight_fields = None
        _highlight_post_tag = None
        _highlight_pre_tag = None
        _minimum_coverage = None
        _order_by = None
        _query_type = None
        _scoring_parameters = None
        _scoring_profile = None
        _search_fields = None
        _search_mode = None
        _select = None
        _skip = None
        _top = None
        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        if search_options is not None:
            _include_total_result_count = search_options.include_total_result_count
            _facets = search_options.facets
            _filter = search_options.filter
            _highlight_fields = search_options.highlight_fields
            _highlight_post_tag = search_options.highlight_post_tag
            _highlight_pre_tag = search_options.highlight_pre_tag
            _minimum_coverage = search_options.minimum_coverage
            _order_by = search_options.order_by
            _query_type = search_options.query_type
            _scoring_parameters = search_options.scoring_parameters
            _scoring_profile = search_options.scoring_profile
            _search_fields = search_options.search_fields
            _search_mode = search_options.search_mode
            _select = search_options.select
            _skip = search_options.skip
            _top = search_options.top
        api_version = "2019-05-06-Preview"

        # Construct URL
        url = self.search_get.metadata['url']
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'indexName': self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if search_text is not None:
            query_parameters['search'] = self._serialize.query("search_text", search_text, 'str')
        if _include_total_result_count is not None:
            query_parameters['$count'] = self._serialize.query("include_total_result_count", _include_total_result_count, 'bool')
        if _facets is not None:
            query_parameters['facet'] = self._serialize.query("facets", _facets, '[str]', div=',')
        if _filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", _filter, 'str')
        if _highlight_fields is not None:
            query_parameters['highlight'] = self._serialize.query("highlight_fields", _highlight_fields, '[str]')
        if _highlight_post_tag is not None:
            query_parameters['highlightPostTag'] = self._serialize.query("highlight_post_tag", _highlight_post_tag, 'str')
        if _highlight_pre_tag is not None:
            query_parameters['highlightPreTag'] = self._serialize.query("highlight_pre_tag", _highlight_pre_tag, 'str')
        if _minimum_coverage is not None:
            query_parameters['minimumCoverage'] = self._serialize.query("minimum_coverage", _minimum_coverage, 'float')
        if _order_by is not None:
            query_parameters['$orderby'] = self._serialize.query("order_by", _order_by, '[str]')
        if _query_type is not None:
            query_parameters['queryType'] = self._serialize.query("query_type", _query_type, 'str')
        if _scoring_parameters is not None:
            query_parameters['scoringParameter'] = self._serialize.query("scoring_parameters", _scoring_parameters, '[str]', div=',')
        if _scoring_profile is not None:
            query_parameters['scoringProfile'] = self._serialize.query("scoring_profile", _scoring_profile, 'str')
        if _search_fields is not None:
            query_parameters['searchFields'] = self._serialize.query("search_fields", _search_fields, '[str]')
        if _search_mode is not None:
            query_parameters['searchMode'] = self._serialize.query("search_mode", _search_mode, 'str')
        if _select is not None:
            query_parameters['$select'] = self._serialize.query("select", _select, '[str]')
        if _skip is not None:
            query_parameters['$skip'] = self._serialize.query("skip", _skip, 'int')
        if _top is not None:
            query_parameters['$top'] = self._serialize.query("top", _top, 'int')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.SearchErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('SearchDocumentsResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    search_get.metadata = {'url': '/docs'}

    async def search_post(
        self,
        search_request: "models.SearchRequest",
        request_options: Optional["models.RequestOptions"] = None,
        **kwargs
    ) -> "models.SearchDocumentsResult":
        """Searches for documents in the index.

        :param search_request: The definition of the Search request.
        :type search_request: ~search_index_client.models.SearchRequest
        :param request_options: Parameter group.
        :type request_options: ~search_index_client.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchDocumentsResult or the result of cls(response)
        :rtype: ~search_index_client.models.SearchDocumentsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SearchDocumentsResult"]
        error_map = kwargs.pop('error_map', {})
        
        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2019-05-06-Preview"

        # Construct URL
        url = self.search_post.metadata['url']
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'indexName': self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(search_request, 'SearchRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.SearchErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('SearchDocumentsResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    search_post.metadata = {'url': '/docs/search.post.search'}

    async def get(
        self,
        key: str,
        selected_fields: Optional[List[str]] = None,
        request_options: Optional["models.RequestOptions"] = None,
        **kwargs
    ) -> object:
        """Retrieves a document from the index.

        :param key: The key of the document to retrieve.
        :type key: str
        :param selected_fields: List of field names to retrieve for the document; Any field not
         retrieved will be missing from the returned document.
        :type selected_fields: list[str]
        :param request_options: Parameter group.
        :type request_options: ~search_index_client.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: object or the result of cls(response)
        :rtype: object
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[object]
        error_map = kwargs.pop('error_map', {})
        
        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2019-05-06-Preview"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'indexName': self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
            'key': self._serialize.url("key", key, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if selected_fields is not None:
            query_parameters['$select'] = self._serialize.query("selected_fields", selected_fields, '[str]')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.SearchErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('object', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/docs(\'{key}\')'}

    async def suggest_get(
        self,
        search_text: str,
        suggester_name: str,
        suggest_options: Optional["models.SuggestOptions"] = None,
        request_options: Optional["models.RequestOptions"] = None,
        **kwargs
    ) -> "models.SuggestDocumentsResult":
        """Suggests documents in the index that match the given partial query text.

        :param search_text: The search text to use to suggest documents. Must be at least 1 character,
         and no more than 100 characters.
        :type search_text: str
        :param suggester_name: The name of the suggester as specified in the suggesters collection
         that's part of the index definition.
        :type suggester_name: str
        :param suggest_options: Parameter group.
        :type suggest_options: ~search_index_client.models.SuggestOptions
        :param request_options: Parameter group.
        :type request_options: ~search_index_client.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SuggestDocumentsResult or the result of cls(response)
        :rtype: ~search_index_client.models.SuggestDocumentsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SuggestDocumentsResult"]
        error_map = kwargs.pop('error_map', {})
        
        _filter = None
        _use_fuzzy_matching = None
        _highlight_post_tag = None
        _highlight_pre_tag = None
        _minimum_coverage = None
        _order_by = None
        _search_fields = None
        _select = None
        _top = None
        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        if suggest_options is not None:
            _filter = suggest_options.filter
            _use_fuzzy_matching = suggest_options.use_fuzzy_matching
            _highlight_post_tag = suggest_options.highlight_post_tag
            _highlight_pre_tag = suggest_options.highlight_pre_tag
            _minimum_coverage = suggest_options.minimum_coverage
            _order_by = suggest_options.order_by
            _search_fields = suggest_options.search_fields
            _select = suggest_options.select
            _top = suggest_options.top
        api_version = "2019-05-06-Preview"

        # Construct URL
        url = self.suggest_get.metadata['url']
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'indexName': self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['search'] = self._serialize.query("search_text", search_text, 'str')
        query_parameters['suggesterName'] = self._serialize.query("suggester_name", suggester_name, 'str')
        if _filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", _filter, 'str')
        if _use_fuzzy_matching is not None:
            query_parameters['fuzzy'] = self._serialize.query("use_fuzzy_matching", _use_fuzzy_matching, 'bool')
        if _highlight_post_tag is not None:
            query_parameters['highlightPostTag'] = self._serialize.query("highlight_post_tag", _highlight_post_tag, 'str')
        if _highlight_pre_tag is not None:
            query_parameters['highlightPreTag'] = self._serialize.query("highlight_pre_tag", _highlight_pre_tag, 'str')
        if _minimum_coverage is not None:
            query_parameters['minimumCoverage'] = self._serialize.query("minimum_coverage", _minimum_coverage, 'float')
        if _order_by is not None:
            query_parameters['$orderby'] = self._serialize.query("order_by", _order_by, '[str]')
        if _search_fields is not None:
            query_parameters['searchFields'] = self._serialize.query("search_fields", _search_fields, '[str]')
        if _select is not None:
            query_parameters['$select'] = self._serialize.query("select", _select, '[str]')
        if _top is not None:
            query_parameters['$top'] = self._serialize.query("top", _top, 'int')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.SearchErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('SuggestDocumentsResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    suggest_get.metadata = {'url': '/docs/search.suggest'}

    async def suggest_post(
        self,
        suggest_request: "models.SuggestRequest",
        request_options: Optional["models.RequestOptions"] = None,
        **kwargs
    ) -> "models.SuggestDocumentsResult":
        """Suggests documents in the index that match the given partial query text.

        :param suggest_request: The Suggest request.
        :type suggest_request: ~search_index_client.models.SuggestRequest
        :param request_options: Parameter group.
        :type request_options: ~search_index_client.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SuggestDocumentsResult or the result of cls(response)
        :rtype: ~search_index_client.models.SuggestDocumentsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SuggestDocumentsResult"]
        error_map = kwargs.pop('error_map', {})
        
        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2019-05-06-Preview"

        # Construct URL
        url = self.suggest_post.metadata['url']
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'indexName': self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(suggest_request, 'SuggestRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.SearchErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('SuggestDocumentsResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    suggest_post.metadata = {'url': '/docs/search.post.suggest'}

    async def index(
        self,
        batch: "models.IndexBatch",
        request_options: Optional["models.RequestOptions"] = None,
        **kwargs
    ) -> "models.IndexDocumentsResult":
        """Sends a batch of document write actions to the index.

        :param batch: The batch of index actions.
        :type batch: ~search_index_client.models.IndexBatch
        :param request_options: Parameter group.
        :type request_options: ~search_index_client.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IndexDocumentsResult or the result of cls(response)
        :rtype: ~search_index_client.models.IndexDocumentsResult or ~search_index_client.models.IndexDocumentsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.IndexDocumentsResult"]
        error_map = kwargs.pop('error_map', {})
        
        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2019-05-06-Preview"

        # Construct URL
        url = self.index.metadata['url']
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'indexName': self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(batch, 'IndexBatch')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 207]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.SearchErrorException.from_response(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('IndexDocumentsResult', pipeline_response)

        if response.status_code == 207:
            deserialized = self._deserialize('IndexDocumentsResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    index.metadata = {'url': '/docs/search.index'}

    async def autocomplete_get(
        self,
        search_text: str,
        suggester_name: str,
        request_options: Optional["models.RequestOptions"] = None,
        autocomplete_options: Optional["models.AutocompleteOptions"] = None,
        **kwargs
    ) -> "models.AutocompleteResult":
        """Autocompletes incomplete query terms based on input text and matching terms in the index.

        :param search_text: The incomplete term which should be auto-completed.
        :type search_text: str
        :param suggester_name: The name of the suggester as specified in the suggesters collection
         that's part of the index definition.
        :type suggester_name: str
        :param request_options: Parameter group.
        :type request_options: ~search_index_client.models.RequestOptions
        :param autocomplete_options: Parameter group.
        :type autocomplete_options: ~search_index_client.models.AutocompleteOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AutocompleteResult or the result of cls(response)
        :rtype: ~search_index_client.models.AutocompleteResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AutocompleteResult"]
        error_map = kwargs.pop('error_map', {})
        
        _x_ms_client_request_id = None
        _autocomplete_mode = None
        _filter = None
        _use_fuzzy_matching = None
        _highlight_post_tag = None
        _highlight_pre_tag = None
        _minimum_coverage = None
        _search_fields = None
        _top = None
        if autocomplete_options is not None:
            _autocomplete_mode = autocomplete_options.autocomplete_mode
            _filter = autocomplete_options.filter
            _use_fuzzy_matching = autocomplete_options.use_fuzzy_matching
            _highlight_post_tag = autocomplete_options.highlight_post_tag
            _highlight_pre_tag = autocomplete_options.highlight_pre_tag
            _minimum_coverage = autocomplete_options.minimum_coverage
            _search_fields = autocomplete_options.search_fields
            _top = autocomplete_options.top
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2019-05-06-Preview"

        # Construct URL
        url = self.autocomplete_get.metadata['url']
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'indexName': self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        query_parameters['search'] = self._serialize.query("search_text", search_text, 'str')
        query_parameters['suggesterName'] = self._serialize.query("suggester_name", suggester_name, 'str')
        if _autocomplete_mode is not None:
            query_parameters['autocompleteMode'] = self._serialize.query("autocomplete_mode", _autocomplete_mode, 'str')
        if _filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", _filter, 'str')
        if _use_fuzzy_matching is not None:
            query_parameters['fuzzy'] = self._serialize.query("use_fuzzy_matching", _use_fuzzy_matching, 'bool')
        if _highlight_post_tag is not None:
            query_parameters['highlightPostTag'] = self._serialize.query("highlight_post_tag", _highlight_post_tag, 'str')
        if _highlight_pre_tag is not None:
            query_parameters['highlightPreTag'] = self._serialize.query("highlight_pre_tag", _highlight_pre_tag, 'str')
        if _minimum_coverage is not None:
            query_parameters['minimumCoverage'] = self._serialize.query("minimum_coverage", _minimum_coverage, 'float')
        if _search_fields is not None:
            query_parameters['searchFields'] = self._serialize.query("search_fields", _search_fields, '[str]')
        if _top is not None:
            query_parameters['$top'] = self._serialize.query("top", _top, 'int')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.SearchErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('AutocompleteResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    autocomplete_get.metadata = {'url': '/docs/search.autocomplete'}

    async def autocomplete_post(
        self,
        autocomplete_request: "models.AutocompleteRequest",
        request_options: Optional["models.RequestOptions"] = None,
        **kwargs
    ) -> "models.AutocompleteResult":
        """Autocompletes incomplete query terms based on input text and matching terms in the index.

        :param autocomplete_request: The definition of the Autocomplete request.
        :type autocomplete_request: ~search_index_client.models.AutocompleteRequest
        :param request_options: Parameter group.
        :type request_options: ~search_index_client.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AutocompleteResult or the result of cls(response)
        :rtype: ~search_index_client.models.AutocompleteResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AutocompleteResult"]
        error_map = kwargs.pop('error_map', {})
        
        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2019-05-06-Preview"

        # Construct URL
        url = self.autocomplete_post.metadata['url']
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'indexName': self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(autocomplete_request, 'AutocompleteRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.SearchErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('AutocompleteResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    autocomplete_post.metadata = {'url': '/docs/search.post.autocomplete'}
