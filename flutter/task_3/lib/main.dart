import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(title: 'Flutter Demo', home: MyHomePage());
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage>
    with SingleTickerProviderStateMixin {
  double _size = 200.0;
  Color color = Colors.blue;

  late AnimationController _controller;
  late Animation _animation;

  void _changeSize() {
    setState(() {
      _size = _size == 200.0 ? 300.0 : 200.0;
      color = Colors.amber;
    });
  }

  @override
  void initState() {
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 1),
    );

    _animation = Tween<double>(begin: 100, end: 300).animate(_controller);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            AnimatedBuilder(
              animation: _animation,
              builder: (context, child) {
                return Container(
                  width: _animation.value,
                  height: _animation.value,
                  color: Colors.deepPurple,
                );
              },
            ),
            Row(
              children: [
                ElevatedButton(
                  child: Text('START'),
                  onPressed: () {
                    _controller.forward();
                  },
                ),
                ElevatedButton(
                  child: Text('END'),
                  onPressed: () {
                    _controller.reverse();
                  },
                ),
              ],
            ),

            const SizedBox(height: 20),
            AnimatedContainer(
              width: _size,
              height: _size,
              duration: const Duration(milliseconds: 500),
              curve: Curves.easeInOut,
              decoration: BoxDecoration(
                color: color,
                borderRadius: BorderRadius.circular(16),
              ),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: _changeSize,
              child: const Text('Змінити розмір'),
            ),
          ],
        ),
      ),
    );
  }

  @override
  void _dispose() {
    _controller.dispose();
    super.dispose();
  }
}
