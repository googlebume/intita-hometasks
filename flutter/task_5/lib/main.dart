import 'package:flutter/material.dart';

/// c309b934254a47d2b58155434251310
void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: const CounterPage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class CounterPage extends StatelessWidget {
  const CounterPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ListView.builder(
        itemCount: 4,
        itemBuilder: (count, index) {
          if (index == 2) return Container(height: 580, color: Colors.amber);
          return Container(height: 580, color: Colors.purple);
        },

      ),
    );
  }
}
