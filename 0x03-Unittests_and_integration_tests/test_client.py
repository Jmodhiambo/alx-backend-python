#!/usr/bin/env python3
"""
Unittests for client.py
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        expected_result = {"login": org_name}
        mock_get_json.return_value = expected_result

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_result)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )


    def test_public_repos_url(self):
        """Test that _public_repos_url returns the expected value"""
        expected_url = "https://api.github.com/orgs/test-org/repos"
        mock_payload = {"repos_url": expected_url}

        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = mock_payload

            client = GithubOrgClient("test-org")
            self.assertEqual(client._public_repos_url, expected_url)


    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test public_repos returns expected repo names"""

        # Sample payload returned by get_json
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        # Mock get_json to return our test payload
        mock_get_json.return_value = test_payload

        # Patch _public_repos_url to avoid using the real org value
        with patch.object(GithubOrgClient, "_public_repos_url", return_value="http://mocked.url"):
            client = GithubOrgClient("test-org")

            # Call the method under test
            repos = client.public_repos()

            # Check the expected result
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])

            # Ensure both mocked methods were called once
            mock_get_json.assert_called_once()
